import asyncio

import aiogram
from aiogram import types
from loader import db, bot, scheduler, dp
from parser_avito import parse

global car_info


async def send_info(message: types.Message):

    caption = "{title}\n<strong>Краткое описание</strong>: {params}\n<u>Цена" \
              "</u>: {price} <b>РУБ</b>\n<strong>Сылка на объявление</strong>: {link}"
    users = await db.get_user_paid(flag_pay=False)
    for i in users:
        user_dict = dict(i)
        if user_dict.get('url_avito') != None:
            print(f"проверка {user_dict.get('full_name')}")
            # await dp.bot.send_message(user_dict.get('telegram_id'), f"{user_dict.get('url_avito')}, {user_dict.get('last_id_drom')}")
            # data = main(user_dict.get('url_avito'), user_dict.get('last_id_drom'))
            # asyncio.run(get_url(user_dict.get('url_avito'), user_dict.get('last_id_drom')))
            data = parse(user_dict.get('url_avito'), user_dict.get('last_id_drom'))
            if len(data) != 0:
                await db.update_last_id_drom(data[0]['link'], user_dict.get('telegram_id'))
                list_params = []
                for j in data:
                    for key, val in j.get('params').items():
                        list_params.append(f'<b>{key}</b>: <em>{val}</em>')
                    try:
                        await dp.bot.send_photo(chat_id=user_dict.get('telegram_id'), photo=j['picture'],
                                                caption=caption.format(params='\n'.join(list_params),
                                                                       price=j['price'],
                                                                       link=j['link'],
                                                                       title=j['title']))
                    except aiogram.utils.exceptions.BotBlocked:
                        await db.delite_user(user_dict.get('telegram_id'))
                        print(f"пользователь {user_dict.get('full_name')} удален")


def add_parsing():
    scheduler.add_job(send_info, "interval", seconds=60, args=(types,))
