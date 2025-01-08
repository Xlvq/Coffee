from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="О нас", callback_data="about"),
         InlineKeyboardButton(text="Меню", callback_data="menu")],
        [InlineKeyboardButton(text="Программа лояльности", callback_data="loyal"),
         InlineKeyboardButton(text="История заказов", callback_data="history")],
        [InlineKeyboardButton(text='Тех.поддержка', callback_data='support')]
    ]
)

return_kb = InlineKeyboardMarkup(
    inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться', callback_data='ret_urn')]
    ]
)

add_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Сиропы', callback_data='add_syrop'),
         InlineKeyboardButton(text='Альтернативное молоко', callback_data='add_milk')],
        [InlineKeyboardButton(text='Другие добавки', callback_data='add_more'),
         InlineKeyboardButton(text='Назад', callback_data='return')]
    ]
)

faq_kb = InlineKeyboardMarkup(
inline_keyboard=[
        [InlineKeyboardButton(text="Отменить заказ", callback_data="stop"),
         InlineKeyboardButton(text="Вопросы по заказу", callback_data="questions")],
        [InlineKeyboardButton(text="Главное меню", callback_data="start")]
    ]
)

questions_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Программа лояльности", callback_data="loyal_program"),
         InlineKeyboardButton(text="Проблема с заказом", callback_data="order_problem")],
        [InlineKeyboardButton(text="Узнать статус заказа", callback_data="order_state"),
         InlineKeyboardButton(text="Другая проблема", callback_data="all_order_problem")],
         [InlineKeyboardButton(text="qwerty", callback_data="l")]
    ]
)




