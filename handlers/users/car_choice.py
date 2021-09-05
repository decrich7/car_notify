from get_last_id_drom import get_id
from keyboards.default.select import beak_seleck_categori
from loader import dp, db
from aiogram import types


from aiogram.dispatcher import FSMContext
from states.state_car import State_celect


@dp.message_handler(text='Добавить категорию автомобилей 🚗')
async def price_min_model(message: types.Message):
    await message.answer('Чтобы добавить категорию перейдите на сайт drom.ru\n'
                         'Выберите марку и модель автомобиля, город, при необходимости поставте другие фильтры'
                         ' и нажмите кнопку показать\n'
                         'Теперь просто скопируйте ссылку и пришлите ее боту\n'
                         'Или нажмите на кнопку поделиться📤 ➡ Telegram ➡ [имя бота]', reply_markup=beak_seleck_categori)
    await State_celect.select_category.set()
