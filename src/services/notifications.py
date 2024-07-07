from src import settings
from src.settings import bot


async def order_notification(coffee_name: str, customer_name: str):
    await bot.send_message(
        settings.ADMIN_ID, f'Заказ <b>"{coffee_name}"</b>\nоформлен клиентом {customer_name}')
