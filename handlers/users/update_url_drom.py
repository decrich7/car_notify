# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher import FSMContext
from get_last_id_drom import get_id
from keyboards.default import beak_update_categori, home
from states.state_car import get_update_url_drom
from loader import dp, db


@dp.message_handler(text='Обновить категорию автомобиля 🚙')
async def bot_start(message: types.Message):
    data_user = await db.select_user(telegram_id=message.from_user.id)
    data_user = dict(data_user)
    if data_user['url_avito'] == None and data_user['last_id_drom'] == None:
        await message.answer('Вы не можете обновить категорию 🤔, сначала нужно ее добавить')

    elif data_user['url_avito'] != None and data_user['last_id_drom'] != None and data_user['flag_pay'] != True:
        await message.answer('Отправте ссылку на новую категорию автомобилей 🚗', reply_markup=beak_update_categori)
        await get_update_url_drom.update_url.set()


@dp.message_handler(state=get_update_url_drom.update_url)
async def price_min_model(message: types.Message, state: FSMContext):
    url_drom = str(message.text)
    if 'https://auto.drom.ru/' in url_drom:
        await state.finish()
        await db.update_last_id_drom(get_id(url_drom), message.from_user.id)
        await db.update_url_avito(url_drom, message.from_user.id)
        await message.answer('Категория автомобилей успешно обновлена🥳', reply_markup=home )
    elif url_drom == 'Я передумал обновлять категорию🤔':
        await state.finish()
        await message.answer('Отмена обновления категории\n', reply_markup=home)
    else:
        await message.answer(
            'К сожалению данная ссылка не подходит, ссылка должна быть с раздела "Автомобили" на drom.ru',
            reply_markup=beak_update_categori)
