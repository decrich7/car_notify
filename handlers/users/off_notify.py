# -*- coding: utf-8 -*-
from aiogram import types
from loader import dp, db
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(text='/off_notify')
async def off_notify(message: types.Message):
    await db.update_url_avito(None, message.from_user.id)
    await db.update_last_id_drom(None, message.from_user.id)
    await message.answer('Уведомления о новых автомобилях отключены 🙁')
