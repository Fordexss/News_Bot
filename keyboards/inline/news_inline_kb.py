from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_news_inline_buttons(news_list: list[dict], category):
    news_inline_markup = InlineKeyboardMarkup()
    for idx, news in enumerate(news_list):
        news_inline_markup.add(InlineKeyboardButton(text=news["header"], callback_data=f"{category}_news{idx}"))
    return news_inline_markup