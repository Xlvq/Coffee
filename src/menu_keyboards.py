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
         InlineKeyboardButton(text="Эспрессо", callback_data="buy_espresso")],
        [InlineKeyboardButton(text="Назад", callback_data="return")]
    ]
)

syrop_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Лаванда", callback_data="syrop_lavender"),
         InlineKeyboardButton(text="Ваниль", callback_data="syrop_vanilla")],
        [InlineKeyboardButton(text="Карамель", callback_data="syrop_caramel"),
         InlineKeyboardButton(text="Банан", callback_data="syrop_banana")],
        [InlineKeyboardButton(text="Миндаль", callback_data="syrop_almond"),
         InlineKeyboardButton(text="Ирландские сливки", callback_data="syrop_irish")],
        [InlineKeyboardButton(text="Кокос", callback_data="syrop_coconut"),
         InlineKeyboardButton(text="Амаретто", callback_data="syrop_amaretto")],
        [InlineKeyboardButton(text="Ананас", callback_data="syrop_pineapple"),
         InlineKeyboardButton(text="Глинтвейн", callback_data="syrop_mulledwine")],
        [InlineKeyboardButton(text="Имбирный пряник", callback_data="syrop_gingerbread"),
         InlineKeyboardButton(text="Кленовый", callback_data="syrop_maple")],
        [InlineKeyboardButton(text="Назад", callback_data="return")]
    ]
)

milk_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Кокосовое", callback_data="milk_coconutmilk"),
         InlineKeyboardButton(text="Овсяное", callback_data="milk_oatmilk")],
        [InlineKeyboardButton(text="Миндальное", callback_data="milk_almondmilk"),
         InlineKeyboardButton(text="Банановое", callback_data="milk_bananamilk")],
        [InlineKeyboardButton(text="Назад", callback_data="return")]
    ]
)

more_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Взбитые сливки", callback_data="more_cream"),
         InlineKeyboardButton(text="Маршмеллоу", callback_data="more_marshmallow")],
        [InlineKeyboardButton(text="Корица", callback_data="more_cinnamon"),
         InlineKeyboardButton(text="Шоколадная крошка", callback_data="more_chocolate")],
         [InlineKeyboardButton(text="Назад", callback_data="return")]
    ]
)