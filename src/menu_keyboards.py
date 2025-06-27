from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Основное меню напитков
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

# Выбор сиропа (можно пропустить)
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
        [InlineKeyboardButton(text="Пропустить", callback_data="syrop_skip"),
         InlineKeyboardButton(text="Назад", callback_data="return")]
    ]
)

# Выбор альтернативного молока (можно пропустить)
milk_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Кокосовое", callback_data="milk_coconutmilk"),
         InlineKeyboardButton(text="Овсяное", callback_data="milk_oatmilk")],
        [InlineKeyboardButton(text="Миндальное", callback_data="milk_almondmilk"),
         InlineKeyboardButton(text="Банановое", callback_data="milk_bananamilk")],
        [InlineKeyboardButton(text="Обычное/нет", callback_data="milk_skip"),
         InlineKeyboardButton(text="Назад", callback_data="return")]
    ]
)

# Дополнительные добавки (можно пропустить)
more_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Взбитые сливки", callback_data="more_cream"),
         InlineKeyboardButton(text="Маршмеллоу", callback_data="more_marshmallow")],
        [InlineKeyboardButton(text="Корица", callback_data="more_cinnamon"),
         InlineKeyboardButton(text="Шоколадная крошка", callback_data="more_chocolate")],
        [InlineKeyboardButton(text="Пропустить", callback_data="more_skip"),
         InlineKeyboardButton(text="Назад", callback_data="return")]
    ]
)

# Выбор объема напитка
volume_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="0.3", callback_data="vol_0.3"),
         InlineKeyboardButton(text="0.4", callback_data="vol_0.4"),
         InlineKeyboardButton(text="0.6", callback_data="vol_0.6")],
        [InlineKeyboardButton(text="Пропустить", callback_data="vol_skip")]
    ]
)

# Меню десертов
dessert_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Чизкейк", callback_data="des_cheesecake"),
         InlineKeyboardButton(text="Маффин", callback_data="des_muffin")],
        [InlineKeyboardButton(text="Нет", callback_data="des_skip")]
    ]
)

# Подтверждение заказа
confirm_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Да", callback_data="confirm_yes"),
         InlineKeyboardButton(text="Нет", callback_data="confirm_no")]
    ]
)

