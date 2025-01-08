from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from src.services.notifications import order_notification
from src import keyboards
from src import menu_keyboards
from src.settings import logger
from src.services.db import get_user_points

router = Router()

orders = {}

@router.message(Command("start"))
@logger.catch
async def start(message: Message):
    await message.answer(
        'Добро пожаловать! Выберите действие:',
        reply_markup=keyboards.start_kb
    )

@router.message(Command("menu"))
@logger.catch
async def menu_kb(message: Message):
    await message.answer_photo(
        photo='https://www.behance.net/gallery/215873575/coffee/modules/1228930415',
        caption='Наше меню:',
        reply_markup=menu_keyboards.menu_kb
    )

@router.callback_query(F.data.startswith("buy"))
@logger.catch
async def select_coffee(callback: CallbackQuery):
    coffee = {
        'raf': 'Раф',
        'latte': 'Латте',
        'ais_raf': 'Айс Раф',
        'ais_latte': 'Айс Латте',
        'americano': 'Американо',
        'cappuccino': 'Капучино',
        'nitro': 'Нитро',
        'espresso': 'Эспрессо'
    }.get(callback.data.split("_")[-1], "Неизвестный напиток")
    orders[callback.from_user.id] = {"coffee": coffee, "customer_name": callback.from_user.full_name}
    logger.debug(f'Клиент {callback.from_user.full_name} выбрал кофе: {coffee}')

    await callback.message.edit_text(
        text=f"Вы выбрали {coffee}. Теперь выберите молоко:",
        reply_markup=menu_keyboards.milk_kb
    )

@router.callback_query(F.data.startswith("milk"))
@logger.catch
async def select_milk(callback: CallbackQuery):
    milk_option = {
        'coconutmilk': 'Кокосовое молоко',
        'oatmilk': 'Овсяное молоко',
        'almondmilk': 'Миндальное молоко',
        'bananamilk': 'Банановое молоко'
    }.get(callback.data.split("_")[-1])

    if milk_option:
        orders[callback.from_user.id]["milk"] = milk_option
        logger.debug(f"Клиент <{callback.from_user.full_name}> выбрал молоко <{milk_option}>")
        await callback.message.edit_text(
            text=f"Вы выбрали: {milk_option}. Теперь выберите сироп:",
            reply_markup=menu_keyboards.syrop_kb
        )
    else:
        logger.warning(f"Неизвестный выбор молока: {callback.data} от пользователя {callback.from_user.full_name}")
        await callback.answer("Неизвестный выбор. Попробуйте снова.", show_alert=True)

@router.callback_query(F.data.startswith("syrop"))
@logger.catch
async def select_syrop_option(callback: CallbackQuery):
    syrop_option = {
        'lavender': 'Лаванда',
        'vanilla': 'Ваниль',
        'caramel': 'Карамель',
        'banana': 'Банан',
        'almond': 'Миндаль',
        'irish': 'Ирландские сливки',
        'coconut': 'Кокос',
        'amaretto': 'Амаретто',
        'pineapple': 'Ананас',
        'mulledwine': 'Глинтвейн',
        'gingerbread': 'Имбирный пряник',
        'maple': 'Кленовый'
    }.get(callback.data.split("_")[-1])

    if syrop_option:
        orders[callback.from_user.id]["syrop"] = syrop_option
        logger.debug(f"Клиент <{callback.from_user.full_name}> выбрал сироп <{syrop_option}>")
        await callback.message.edit_text(
            text=f"Вы выбрали сироп: {syrop_option}. Теперь выберите другие добавки:",
            reply_markup=menu_keyboards.more_kb
        )
    else:
        logger.warning(f"Неизвестный выбор сиропа: {callback.data} от пользователя {callback.from_user.full_name}")
        await callback.answer("Неизвестный выбор. Попробуйте снова.", show_alert=True)

@router.callback_query(F.data.startswith("more"))
@logger.catch
async def select_additional_additions(callback: CallbackQuery):
    addition = {
        'cream': 'Взбитые сливки',
        'marshmallow': 'Маршмеллоу',
        'cinnamon': 'Корица',
        'chocolate': 'Шоколадная крошка'
    }.get(callback.data.split("_")[-1])

    if addition:
        if "additions" not in orders[callback.from_user.id]:
            orders[callback.from_user.id]["additions"] = []
        orders[callback.from_user.id]["additions"].append(addition)
        logger.debug(f"Клиент <{callback.from_user.full_name}> выбрал добавку <{addition}>")
        await callback.message.edit_text(
            text=f"Вы выбрали: {addition}. Спасибо за заказ!",
            reply_markup=keyboards.faq_kb
        )
    else:
        logger.warning(f"Неизвестный выбор добавки: {callback.data} от пользователя {callback.from_user.full_name}")
        await callback.answer("Неизвестный выбор. Попробуйте снова.", show_alert=True)

    await order_notification(
                orders[callback.from_user.id]["coffee"],
                orders[callback.from_user.id]["customer_name"],
                orders[callback.from_user.id].get("milk"),
                orders[callback.from_user.id].get("syrop"),
                orders[callback.from_user.id].get("additions", [])
            )

@router.callback_query(F.data == "menu")
@logger.catch
async def menu_func(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Меню:",
        reply_markup=menu_keyboards.menu_kb
    )

@router.callback_query(F.data == "return")
@logger.catch
async def go_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Меню:",
        reply_markup=menu_keyboards.menu_kb
    )
@router.callback_query(F.data == "questions")
@logger.catch
async def qstns(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Выберете действие:",
        reply_markup=keyboards.questions_kb
    )
@router.callback_query(F.data == "stop")
@logger.catch
async def stop(callback: CallbackQuery):
    await callback.message.edit_text(
        text="уже поздно!",
    )

@router.callback_query(F.data == "support")
@logger.catch
async def support(callback: CallbackQuery):
    await callback.message.edit_text(
        text="",
        reply_markup=keyboards.questions_kb
    )

@router.callback_query(F.data == "loyal_program")
@logger.catch
async def loyal_program(callback: CallbackQuery):
    user_id = callback.from_user.id
    coins = await get_user_points(user_id)
    await callback.message.edit_text(
        text=f"У вас {coins} баллов",
        reply_markup=keyboards.return_kb
    )








