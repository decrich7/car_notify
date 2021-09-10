import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import datetime as dt
from aiogram.dispatcher import FSMContext

from keyboards.default import brand_select, home
from states.state_car import State_celect
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username,
                                 time=dt.datetime.now().strftime("%d-%m-%y %H:%M:%S"),
                                 url_avito=None,
                                 flag_pay=False,
                                 last_id_drom=None)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer(f'Здравствуйте👋, {message.from_user.full_name}!\n', reply_markup=home)
