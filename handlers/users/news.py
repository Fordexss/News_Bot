import random

from aiogram import types

from keyboards.default import news_categories
from keyboards.inline import create_news_inline_buttons
from loader import dp
from parser_news.parser import db_of_news

NEWS_CATEGORIES = tuple(db_of_news.keys())


@dp.message_handler(commands="whattoread")
async def bot_what_to_read(message: types.Message):
    await message.answer("Які новини вас цікавлять?", reply_markup=news_categories)


# lambda msg: msg.text in NEWS_CATEGORIES
@dp.message_handler(text=NEWS_CATEGORIES)
async def bot_new_categories(message: types.Message):
    category = message.text
    inline_kb = create_news_inline_buttons(db_of_news[category], category)
    await message.answer("Натисніть на відповідну кнопку для отримання новини", reply_markup=inline_kb)


@dp.callback_query_handler(lambda call: '_news' in call.data)
async def bot_show_news(call: types.CallbackQuery):
    category, indx_of_news = call.data.split('_news')
    news = db_of_news[category][int(indx_of_news)]
    await call.message.answer(
        f"<b>{news['header']}</b>\n\n"
        f"{news['body_text']}\n"
        f"Джерело - {news['link']}",
        parse_mode="HTML"
    )


@dp.message_handler(commands="randomtopic")
async def random_news_topic(message: types.Message):
    choice = random.choice(NEWS_CATEGORIES)
    news_len = random.choice(range(len(db_of_news[choice])))
    random_news = db_of_news[choice][int(news_len)]
    await message.answer(
        f"<b>{random_news['header']}</b>\n\n"
        f"{random_news['body_text']}\n"
        f"Джерело - {random_news['link']}",
        parse_mode="HTML")
