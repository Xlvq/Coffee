from src import settings
from src.settings import bot


# Функция для отправки уведомлений админу о заказе
async def order_notification(coffee_name: str, customer_name: str, milk: str = None, syrop: str = None,
                             additions: list = None):
    additions_str = ', '.join(additions) if additions else 'Нет дополнительных добавок'
    message = f'Заказ <b>"{coffee_name}"</b>\n'
    message += f'Клиент: {customer_name}\n'
    message += f'Молоко: {milk if milk else "Не указано"}\n'
    message += f'Сироп: {syrop if syrop else "Не указано"}\n'
    message += f'Дополнительные добавки: {additions_str}'

    await bot.send_message(settings.ADMIN_ID, message)
