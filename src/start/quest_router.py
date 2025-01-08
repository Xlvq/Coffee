from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from src.services.notifications import order_notification
from src import keyboards
from src.settings import logger


quest = Router()

@quest.callback_query(F.data == "loyal_program")
@logger.catch

async def loyal_program(callback: CallbackQuery):
    await callback.message.edit_text(
        text=('Поддержка:'),
        reply_markup=keyboards.return_kb
    )

@quest.callback_query(F.data == "order_problem")
@logger.catch
async def order_problem(callback: CallbackQuery):
    await callback.message.edit_text(
        text=".........",
        reply_markup=keyboards.return_kb
    )
@quest.callback_query(F.data == "order_state")
@logger.catch
async def order_state(callback: CallbackQuery):
    await callback.message.edit_text(
        text="н",
        reply_markup=keyboards.return_kb
    )
@quest.callback_query(F.data == 'all_order_problem')
@logger.catch
async def all_order_problem(callback: CallbackQuery):
    await callback.message.edit_text(
        text="назад",
        reply_markup=keyboards.return_kb
    )
# @quest.callback_query(F.data == "loyal_program")
# @logger.catch
# async def loyal_programm(callback: CallbackQuery):
#     await callback.message.edit_text(
#         text="назад",
#         reply_markup=keyboards.return_kb
#     )