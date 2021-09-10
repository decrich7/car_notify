from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Главное меню',
        '/off_notify - Отключить уведомления о новых объявлениях удалив добавленную категорию',
        '/help - Выводит список команд',
        "/spravka - Показывает информацию о боте"
    ]
    await message.answer('\n'.join(text))


@dp.message_handler(text='Команды 📱')
async def send_command(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Главное меню',
        '/off_notify - Отключить уведомления о новых объявлениях удалив добавленную категорию',
        '/help - Выводит список команд',
        "/spravka - Показывает информацию о боте"

    ]
    await message.answer('\n'.join(text))
