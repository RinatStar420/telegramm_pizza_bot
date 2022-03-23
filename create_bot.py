from aiogram import Bot, Dispatcher
import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage # этот класс позволяет хранить данные в оперативной памяти


"""Данный файл создан для производства взаимоимпортов между хендлерами и ботом"""
storage = MemoryStorage()
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=storage)


