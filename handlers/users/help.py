from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Розпочати діалог",
            "/help - Вивести справку",
            "/whattoread - Обрати новину з певних категорій",
            "/randomtopic - Випадкова новина з нашої бази")
    
    await message.answer("\n".join(text))
