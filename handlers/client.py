from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

"""***************************************Клиентская часть******************************************"""
class Client:

    # @dp.message_handler(commands=['start', 'help'])
    def __init__(self, address, work_time):
        self.address = address
        self.work_time = work_time

    @classmethod
    async def command_start(cls, message: types.Message) -> None:
        try:
            await bot.send_message(message.from_user.id, 'Приятного аппетита',
                                   reply_markup=kb_client)  # reply_markup=kb_client - передаю в команду старт клавиатуру
            await message.delete()
        except:
            await message.reply(
                'Общение с ботом через ЛС, напишите ему:\n https://t.me/Pizza_vivaBot')  # для упоминания сообщения на которое отправляется ответ


    # @dp.message_handler(commands=['Режим_работы'])
    async def pizza_open_command(self, message: types.Message):
        await bot.send_message(message.from_user.id, self.work_time)



    # @dp.message_handler(commands=['Расположение'])
    async def pizza_place_command(self, message: types.Message):
        await bot.send_message(message.from_user.id, self.address,
                                   reply_markup=ReplyKeyboardRemove())  # reply_markup=ReplyKeyboardRemove удаляет клавиатуру после нажания определенной команды



    # @dp.message_handler(commands=['Меню'])
    async def pizza_menu_command(self, message : types.Message):
        await sqlite_db.sql_read(message)


    def register_handlers_client(self, dp: Dispatcher):
        dp.register_message_handler(self.command_start, commands=['start', 'help'])
        dp.register_message_handler(self.pizza_open_command, commands=['Режим_работы'])
        dp.register_message_handler(self.pizza_place_command, commands=['Расположение'])
        dp.register_message_handler(self.pizza_menu_command, commands=['Меню'])


