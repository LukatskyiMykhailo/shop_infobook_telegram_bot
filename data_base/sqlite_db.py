import sqlite3 as sq
from create_bot import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def sql_start():
    global base, cur
    base = sq.connect('products.db')
    cur = base.cursor()
    if base:
        print('DB connected!!!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, categories TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT, url TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT OR IGNORE INTO menu VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def kat1_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%PREVELOSS%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))


async def kat2_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%COLORE%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat3_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%KERATINÈ%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat4_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%NUTRIÈ%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat5_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%ARGANE%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat6_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%VOLUMÈ%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat7_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%TWIN%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat8_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%AREA TECHNICA%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat9_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%MULTIVITAM%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat10_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%glass zalupa%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat11_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%glass zalupa%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat12_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%glass zalupa%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))

async def kat13_read(message):
    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%glass zalupa%'").fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'\n{ret[2]}\n\n{ret[3]}\n\nЦіна: {ret[4]} грн', reply_markup=InlineKeyboardMarkup().\
            add(InlineKeyboardButton(text='Замовити', url=ret[-1])))



#async def sql_read(message):
#    for ret in cur.execute("SELECT * FROM menu WHERE categories LIKE'%glass zalupa%'").fetchall():
#        await bot.send_photo(message.from_user.id, ret[0], f'\nНазва: {ret[2]}\nОпис: {ret[3]}\nЦіна: {ret[-1]}')
