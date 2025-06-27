from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from src import keyboards, menu_keyboards
from src.settings import logger
from src.services.db import (
    get_user_points,
    add_order,
    get_user_orders,
)
from src.services.notifications import order_notification
from src.services.payments import send_invoice

router = Router()

# текущие заказы пользователей
orders: dict[int, dict] = {}

# доступные промокоды
PROMO_CODES = {"SALE10": 10}


@router.message(Command("start"))
@logger.catch
async def start(message: Message):
    await message.answer(
        "Добро пожаловать! Выберите действие:", reply_markup=keyboards.start_kb
    )


@router.message(Command("menu"))
@logger.catch
async def menu_command(message: Message):
    await message.answer("Наше меню:", reply_markup=menu_keyboards.menu_kb)


@router.callback_query(F.data.startswith("buy"))
@logger.catch
async def select_coffee(callback: CallbackQuery):
    coffee = {
        "raf": "Раф",
        "latte": "Латте",
        "ais_raf": "Айс Раф",
        "ais_latte": "Айс Латте",
        "americano": "Американо",
        "cappuccino": "Капучино",
        "nitro": "Нитро",
        "espresso": "Эспрессо",
    }.get(callback.data.split("_")[-1], "Неизвестно")

    orders[callback.from_user.id] = {
        "coffee": coffee,
        "customer_name": callback.from_user.full_name,
    }
    logger.debug(f"Клиент {callback.from_user.full_name} выбрал кофе: {coffee}")

    if coffee == "Эспрессо":
        await callback.message.edit_text(
            text=f"Вы выбрали {coffee}. Хотите десерт?",
            reply_markup=menu_keyboards.dessert_kb,
        )
    else:
        await callback.message.edit_text(
            text=f"Вы выбрали {coffee}. Выберите объем:",
            reply_markup=menu_keyboards.volume_kb,
        )


@router.callback_query(F.data.startswith("vol"))
@logger.catch
async def select_volume(callback: CallbackQuery):
    uid = callback.from_user.id
    code = callback.data.split("_")[1]
    orders[uid]["volume"] = None if code == "skip" else code
    await callback.message.edit_text(
        text="Выберите молоко:", reply_markup=menu_keyboards.milk_kb
    )


@router.callback_query(F.data.startswith("milk"))
@logger.catch
async def select_milk(callback: CallbackQuery):
    uid = callback.from_user.id
    milk_option = {
        "coconutmilk": "Кокосовое",
        "oatmilk": "Овсяное",
        "almondmilk": "Миндальное",
        "bananamilk": "Банановое",
        "skip": "Обычное/нет",
    }.get(callback.data.split("_")[-1])

    orders[uid]["milk"] = milk_option
    await callback.message.edit_text(
        text="Выберите сироп:", reply_markup=menu_keyboards.syrop_kb
    )


@router.callback_query(F.data.startswith("syrop"))
@logger.catch
async def select_syrop(callback: CallbackQuery):
    uid = callback.from_user.id
    syrop_option = {
        "lavender": "Лаванда",
        "vanilla": "Ваниль",
        "caramel": "Карамель",
        "banana": "Банан",
        "almond": "Миндаль",
        "irish": "Ирландские сливки",
        "coconut": "Кокос",
        "amaretto": "Амаретто",
        "pineapple": "Ананас",
        "mulledwine": "Глинтвейн",
        "gingerbread": "Имбирный пряник",
        "maple": "Кленовый",
        "skip": None,
    }.get(callback.data.split("_")[-1])

    orders[uid]["syrup"] = syrop_option
    await callback.message.edit_text(
        text="Выберите дополнительные добавки:",
        reply_markup=menu_keyboards.more_kb,
    )


@router.callback_query(F.data.startswith("more"))
@logger.catch
async def select_more(callback: CallbackQuery):
    uid = callback.from_user.id
    addition = {
        "cream": "Взбитые сливки",
        "marshmallow": "Маршмеллоу",
        "cinnamon": "Корица",
        "chocolate": "Шоколадная крошка",
        "skip": None,
    }.get(callback.data.split("_")[-1])

    if addition:
        orders.setdefault(uid, {}).setdefault("additions", []).append(addition)

    await callback.message.edit_text(
        text="Хотите десерт?",
        reply_markup=menu_keyboards.dessert_kb,
    )


@router.callback_query(F.data.startswith("des"))
@logger.catch
async def select_dessert(callback: CallbackQuery):
    uid = callback.from_user.id
    dessert = {
        "cheesecake": "Чизкейк",
        "muffin": "Маффин",
        "skip": None,
    }.get(callback.data.split("_")[-1])

    orders[uid]["dessert"] = dessert
    orders[uid]["stage"] = "promo"
    await callback.message.edit_text(
        text="Если у вас есть промокод, отправьте его сообщением. Или нажмите 'Вернуться' чтобы пропустить",
        reply_markup=keyboards.return_kb,
    )


@router.message(F.text)
@logger.catch
async def promo_handler(message: Message):
    data = orders.get(message.from_user.id)
    if not data or data.get("stage") != "promo":
        return

    code = message.text.strip().upper()
    discount = PROMO_CODES.get(code)
    if discount:
        data["promo_code"] = code
        data["discount"] = discount
        await message.answer(f"Промокод {code} применен (-{discount}% ).")
    else:
        await message.answer("Неверный промокод. Пропускаем.")
    data["stage"] = "confirm"
    await send_summary(message, data)


@router.callback_query(F.data == "ret_urn")
@logger.catch
async def promo_skip(callback: CallbackQuery):
    data = orders.get(callback.from_user.id)
    if data and data.get("stage") == "promo":
        data["promo_code"] = None
        data["discount"] = 0
        data["stage"] = "confirm"
        await send_summary(callback.message, data)


async def send_summary(target, data):
    text = f"Вы заказали {data['coffee']}"
    if data.get("volume"):
        text += f" {data['volume']} л"
    if data.get("milk"):
        text += f"\nМолоко: {data['milk']}"
    if data.get("syrup"):
        text += f"\nСироп: {data['syrup']}"
    additions = ", ".join(data.get("additions", [])) if data.get("additions") else "Нет"
    text += f"\nДобавки: {additions}"
    text += f"\nДесерт: {data.get('dessert', 'Нет')}"
    if data.get("promo_code"):
        text += f"\nПромокод: {data['promo_code']} (-{data['discount']}%)"
    await target.answer(text, reply_markup=menu_keyboards.confirm_kb)


@router.callback_query(F.data == "confirm_yes")
@logger.catch
async def confirm_yes(callback: CallbackQuery):
    uid = callback.from_user.id
    order = orders.pop(uid, None)
    if not order:
        await callback.message.edit_text("Заказ не найден.")
        return
    order_id = await add_order(
        uid,
        order["coffee"],
        order.get("volume"),
        order.get("milk"),
        order.get("syrup"),
        order.get("additions"),
        order.get("dessert"),
        order.get("promo_code"),
    )
    await callback.message.edit_text(f"Заказ #{order_id} создан. Оплатите заказ.")
    await send_invoice(uid, order_id, 200)
    await order_notification(
        order["coffee"],
        order["customer_name"],
        order.get("milk"),
        order.get("syrup"),
        order.get("additions", []),
    )


@router.callback_query(F.data == "confirm_no")
@logger.catch
async def confirm_no(callback: CallbackQuery):
    orders.pop(callback.from_user.id, None)
    await callback.message.edit_text("Заказ отменен", reply_markup=keyboards.start_kb)


@router.callback_query(F.data == "menu")
@logger.catch
async def menu_callback(callback: CallbackQuery):
    await callback.message.edit_text("Меню:", reply_markup=menu_keyboards.menu_kb)


@router.callback_query(F.data == "return")
@logger.catch
async def go_back(callback: CallbackQuery):
    await callback.message.edit_text("Меню:", reply_markup=menu_keyboards.menu_kb)


@router.callback_query(F.data == "questions")
@logger.catch
async def qstns(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберете действие:", reply_markup=keyboards.questions_kb
    )


@router.callback_query(F.data == "support")
@logger.catch
async def support(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Поддержка:", reply_markup=keyboards.questions_kb
    )


@router.callback_query(F.data == "loyal_program")
@logger.catch
async def loyal_program(callback: CallbackQuery):
    user_id = callback.from_user.id
    coins = await get_user_points(user_id)
    await callback.message.edit_text(
        text=f"У вас {coins} баллов", reply_markup=keyboards.return_kb
    )


@router.callback_query(F.data == "history")
@logger.catch
async def history(callback: CallbackQuery):
    records = await get_user_orders(callback.from_user.id)
    if not records:
        text = "История пуста"
    else:
        lines = [f"#{r[0]} {r[1]} - {r[2]} ({r[3]})" for r in records]
        text = "\n".join(lines)
    await callback.message.edit_text(text, reply_markup=keyboards.return_kb)
