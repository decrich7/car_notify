# -*- coding: utf-8 -*-
from aiogram import types
from loader import dp
from aiogram.types import ReplyKeyboardRemove



@dp.message_handler(text='Справка 📜')
async def get_spravka(message: types.Message):
    await message.answer(f'[имя бота] - это сервис который поможет отслеживать появление новых объявлений'
                         ' по выбранной вами категории автомобилей 🚘 на интернет-портале drom.ru\n'
                         'После добавления категории авто, бот будет просматривать ее, и при появлении новых объявлений'
                         ', уведомит вас о них, прислав ссылку на него и краткую информацию с фотографией автомобиля\n'
                         'Чтобы начать нажмите кнопку - "Добавить категорию"')