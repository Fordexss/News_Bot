from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустити бота"),
            types.BotCommand("help", "Вивести справку"),
            types.BotCommand("whattoread", "Обрати новину"),
            types.BotCommand("randomtopic", "Випадкова новина"),
        ]
    )
