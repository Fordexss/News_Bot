from aiogram import types

from loader import dp


@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message):
    await message.answer("На жаль, це невідома мені команда, введіть /help для справки")
