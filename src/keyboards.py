from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Раф", callback_data="buy_raf"),
         InlineKeyboardButton(text="Латте", callback_data="buy_latte")],
        [InlineKeyboardButton(text="Айс раф", callback_data="buy_ais_raf"),
         InlineKeyboardButton(text="Айс латте", callback_data="buy_ais_latte")],
        [InlineKeyboardButton(text="Американо", callback_data="buy_americano"),
         InlineKeyboardButton(text="Капучино", callback_data="buy_cappuccino")],
        [InlineKeyboardButton(text="Нитро", callback_data="buy_nitro"),
         InlineKeyboardButton(text="Эспрессо", callback_data="buy_espresso")]
    ]
)
