from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("spravka", "Показывает информацию о боте"),
        types.BotCommand("off_notify", "Отключить уведомления о новых объявлениях удалив добавленную категорию"),
        types.BotCommand("help", "Выводит список команд"),
    ])
