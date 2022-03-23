from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# KeyboardButton - непосредственно сама кнопка и она же отпровляет команду

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('/Поделиться номером', request_contact=True)
# b5 = KeyboardButton('/Отправить где я', request_location=True)

#ReplyKeyboardMarkup - заменяет обычную клаву на ту, которую я создам
kb_client = ReplyKeyboardMarkup(resize_keyboard=True) # resize_keyboard=True делает размер кнопки под то, что там написано
# one_time_keyboard=True отвечает за то, чтобы после нажатия кнопки клавиатура скрывалась
kb_client.add(b1).add(b2).add(b3) #.row(b4, b5)

# метод add() - добовляет кнопку с новой строки
# метод insert() - добовляет кнопку в ряд, если есть место
# метод row() - добовляет все кнопки в одну строку
# все эти методы можно компоновать как удобно