from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db

class FSMAdmin(StatesGroup):
    photo = State()
    categories = State()
    name = State()
    description = State()
    price = State()
    url = State()

async def cm_start(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Upload photo')

async def cancel_handler(message: types.Message, state:FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Stoped')

async def load_photo(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Take categories')

async def load_categories (message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['categories'] = message.text
    await FSMAdmin.next()
    await message.reply('Take name')

async def load_name (message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Take description')

async def load_description (message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Take price')

async def load_price (message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    await FSMAdmin.next()
    await message.reply('Take url')

async def load_url (message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['url'] = message.text

    await sqlite_db.sql_add_command(state)
    await state.finish()
    await message.reply('End!')



def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Down'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_categories, state=FSMAdmin.categories)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(load_url, state=FSMAdmin.url)
