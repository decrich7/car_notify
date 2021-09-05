import logging
from aiogram import executor
from loader import dp, db, scheduler, types
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from handlers.users.VREMENNO import add_parsing


async def on_startup(dispatcher):
    # Уведомляет про запуск
    logging.info("Создаем подключение к базе данных")
    await db.create()
    # await db.delete_users()
    logging.info("Создаем таблицу пользователей")
    await db.create_table_users()
    logging.info("Готово.")
    add_parsing()
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
