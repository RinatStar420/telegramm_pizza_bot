from aiogram import types, Dispatcher
import string
import json


# from bot import dp, bot

"""*****************************************Общая часть******************************************"""

# обработчик с пустыми скобками улавливает любые сообщения, которые отправляются боту (пустой обработчик нееобходимо распологать внизу кода)
# блягодаря пустым скобкам можно выстраивать проверки входящих сообщений путём if/elif/elso

# @dp.message_handler()
async def echo(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()

        # await message.answer(message.text)  """1 метод - просто отвечает на сообщение"""
        # await message.reply(message.text) """2 метод - отвечает  на сообщение упоминая автора"""
        # await bot.send_message(message.from_user.id, message.text) """3 метод - если написать в группу, то бот ответит в личку (если добавить бота в друзья)"""


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo)
