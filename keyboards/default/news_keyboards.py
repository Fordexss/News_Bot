from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

news_categories = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Економічні новини"), KeyboardButton(text="Політичні новини")],
        [KeyboardButton(text="Cуспільні новини"), KeyboardButton(text="Міжнародні новини")],
    ],
    resize_keyboard=True
)
