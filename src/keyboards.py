from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Раф", callback_data="buy_raf")],
        [InlineKeyboardButton(text="Латте", callback_data="buy_latte")],
        [InlineKeyboardButton(text="Айс раф", callback_data="buy_ais_raf")],
        [InlineKeyboardButton(text="Айс латте", callback_data="buy_ais_latte")],
    ]
)
