from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


butt1 = KeyboardButton('/Каталог')
butt2 = KeyboardButton('/Головне')
butt3 = KeyboardButton('/Додатково')
butt4 = KeyboardButton('/Відправити', request_contact=True)
butt5 = KeyboardButton('/Головна')


shkb = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
in_kb = InlineKeyboardMarkup(row_width=3)


butt6 = InlineKeyboardButton(text='PREVELOSS', callback_data='Kat1')
butt7 = InlineKeyboardButton(text='COLORE', callback_data='Kat2')
butt8 = InlineKeyboardButton(text='KERATINÈ', callback_data='Kat3')
butt9 = InlineKeyboardButton(text='NUTRIÈ', callback_data='Kat4')
butt10 = InlineKeyboardButton(text='ARGANE', callback_data='Kat5')
butt11 = InlineKeyboardButton(text='VOLUMÈ', callback_data='Kat6')
butt12 = InlineKeyboardButton(text='TWIN', callback_data='Kat7')
butt13 = InlineKeyboardButton(text='AREA TECHNICA', callback_data='Kat8')
butt14 = InlineKeyboardButton(text='MULTIVITAM', callback_data='Kat9')
butt15 = InlineKeyboardButton(text='Kat10', callback_data='Kat10')
butt16 = InlineKeyboardButton(text='Kat11', callback_data='Kat11')
butt17 = InlineKeyboardButton(text='Kat12', callback_data='Kat12')
butt18 = InlineKeyboardButton(text='Kat13', callback_data='Kat13')


kb_client.add(butt1).add(butt2)
shkb.add(butt4)
in_kb.add(butt6, butt7, butt8, butt9, butt10, butt11, butt12, butt13, butt14)
