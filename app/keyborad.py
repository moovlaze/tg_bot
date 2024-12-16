from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Каталог")],
        [KeyboardButton(text="Корзина")],
        [KeyboardButton(text="Контакты"), KeyboardButton(text="О нас")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Футболки", callback_data="t-shirt")],
        [InlineKeyboardButton(text="Джинсы", callback_data="jeans")],
        [
            InlineKeyboardButton(text="Кроссовки", callback_data="sneakers"),
            InlineKeyboardButton(text="Носки", callback_data="socks"),
        ],
    ]
)

get_number = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Отправить номер", request_contact=True)]],
    resize_keyboard=True,
)
