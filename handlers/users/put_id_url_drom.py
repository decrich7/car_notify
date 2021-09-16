from aiogram.types import ReplyKeyboardRemove

from get_last_id_drom import get_id
from keyboards.default import beak_seleck_categori, home
from loader import dp, db
from aiogram import types

from aiogram.dispatcher import FSMContext
from states.state_car import State_celect


@dp.message_handler(state=State_celect.select_category)
async def price_min_model(message: types.Message, state: FSMContext):
    url_drom = str(message.text)
    if 'https://auto.drom.ru/' in url_drom:
        try:
            await db.update_last_id_drom(get_id(url_drom), message.from_user.id)
            await state.finish()
            await db.update_last_id_drom(get_id(url_drom), message.from_user.id)
            await db.update_url_avito(url_drom, message.from_user.id)
            await message.answer(
                'Категория успешно добавлена🙃\n'
                'При появлении новых объявлений, мы вас оповестим🤓', reply_markup=home)
        except:
            await message.reply('Данная ссылка не работает 🙁 \n'
                                'Пожалуйста, проверте ее, и прешлите валидную ссылку 😊')

    elif url_drom == 'Я передумал добавлять категорию🤔':
        await state.finish()
        await message.answer('Отмена выбора категории\n', reply_markup=home)
    else:
        await message.reply(
            'К сожалению данная ссылка не подходит, ссылка должна быть с раздела "Автомобили" на drom.ru',
            reply_markup=beak_seleck_categori)
