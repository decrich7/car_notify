from get_last_id_drom import get_id
from keyboards.default.select import beak_seleck_categori
from loader import dp, db
from aiogram import types


from aiogram.dispatcher import FSMContext
from states.state_car import State_celect


@dp.message_handler(text='Добавить категорию автомобилей 🚗')
async def price_min_model(message: types.Message):
    data = dict(await db.select_user(telegram_id=message.from_user.id))
    if data.get('url_avito') == None:
        await message.answer('Чтобы добавить категорию перейдите на сайт drom.ru\n'
                             'Выберите марку и модель автомобиля, город, при необходимости поставте другие фильтры'
                             ' и нажмите кнопку <b>Показать</b>\n'
                             'Теперь просто скопируйте ссылку и пришлите ее боту\n'
                             'Либо же нажмите на кнопку поделиться📤 ➡ Telegram ➡ Car Notify', reply_markup=beak_seleck_categori)
        await State_celect.select_category.set()
    else:
        await message.answer('У вас уже добавлена категория 🤨\n'
                             'Если вы хотите обновить ее, нажмите на кнопку "Обновить категорию автомобиля 🚙"')



