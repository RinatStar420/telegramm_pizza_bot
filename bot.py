import logging
from aiogram import executor
from create_bot import dp
from data_base import sqlite_db




logging.basicConfig(level=logging.INFO)


async def bot_on_startup(_):
    print("я тестовая функцая, чтобы проверить добавление статической функции в executor")
    sqlite_db.start_sql()


from handlers.client import Client
from handlers import other, admin

user = Client('ул.Колбасная', '24/7')
user.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_on_startup)
