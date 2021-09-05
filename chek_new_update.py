from aiogram import types
import asyncio
from loader import db, bot
from parser_avito import avito_parse

@bot.message_handler(text='салам')
async def send_info(message: types.Message):
    caption = """{title}\nКраткое описание:  {params}\nАдрес:  {geo}\n
              <u>Цена: </u> {price} <b>RUB</b>\n
              Сылка на объявление: {link}"""
    users = await db.get_user_paid(flag_pay=False)
    for i in users:
        # asyncio.sleep(10)
        user_dict = dict(i)
        data = avito_parse(user_dict('url_avito'), '№ 2150652741')
        await bot.send_photo(chat_id=user_dict.get('telegram_id'), photo=data['picture'],
                             caption=caption.format(params=data['params'],
                                                    price=data['price'],
                                                    geo=data['geo'],
                                                    link=data['link'],
                                                    title=data['title']))
