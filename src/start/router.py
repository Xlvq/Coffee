from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from src import keyboards
from src.services.notifications import order_notification
from src.settings import logger, bot

router = Router()


@router.message(Command("start"))
@logger.catch
async def start(message: Message):
    await message.answer_photo(
        'https://static.ivkrak.ru/static/photos/e4b7c59d-9537-425b-91a4-ac87e15a0d72.jpg',
        # можно выложить в ВК или ещё куда-нибудь, и скопировать ссылку на фотку
        caption='Меню',
        reply_markup=keyboards.menu_kb
    )


@router.callback_query(F.data.startswith("buy"))
@logger.catch
async def menu(qq: CallbackQuery):
    coffee = {
        'raf': 'Раф',
        'latte': 'Латте',
        'ais_raf': 'Айс Раф',
        'ais_latte': 'Айс Латте'
    }.get(qq.data.split("_")[-1])
    logger.debug(f'Клиент <{qq.from_user.full_name}> заказал <{coffee}>')
    await order_notification(coffee, qq.from_user.full_name)
    await qq.answer('Заказ оформлен', show_alert=True)