from src.settings import bot
from src.services.db import update_order_status

async def send_invoice(user_id: int, order_id: int, amount: int) -> None:
    link = f"https://pay.yookassa.ru/demo?order={order_id}&amount={amount}"
    await bot.send_message(user_id, f"Ссылка для оплаты заказа #{order_id}: {link}")
    await update_order_status(order_id, "Оплата")

