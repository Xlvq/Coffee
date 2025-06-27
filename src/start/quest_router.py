from aiogram import Router, F
from aiogram.types import CallbackQuery
from src.services.db import get_user_orders
from src import keyboards
from src.settings import logger

quest = Router()

@quest.callback_query(F.data == "loyal_program")
@logger.catch
async def loyal_program(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Поддержка:",
        reply_markup=keyboards.return_kb
    )

@quest.callback_query(F.data == "order_problem")
@logger.catch
async def order_problem(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Опишите проблему сообщением, мы свяжемся с вами.",
        reply_markup=keyboards.return_kb
    )

@quest.callback_query(F.data == "order_state")
@logger.catch
async def order_state(callback: CallbackQuery):
    orders = await get_user_orders(callback.from_user.id)
    if orders:
        order_id, coffee, status, created = orders[0]
        text = f"Ваш последний заказ #{order_id} ({coffee}) имеет статус: {status}"
    else:
        text = "У вас нет активных заказов."
    await callback.message.edit_text(text, reply_markup=keyboards.return_kb)

@quest.callback_query(F.data == "all_order_problem")
@logger.catch
async def all_order_problem(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Свяжитесь с нами в чате @support, мы поможем!",
        reply_markup=keyboards.return_kb
    )

