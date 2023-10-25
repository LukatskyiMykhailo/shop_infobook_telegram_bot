from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, shkb, in_kb
from data_base import sqlite_db
import sqlite3
import aiogram.utils.markdown as fmt


async def command_start(message : types.Message):
	await bot.send_message(message.from_user.id,
		fmt.text(
			fmt.text("Привіт 🤗"),
			fmt.text(""),
			fmt.text("Це  BIOSKY-бот ,аби ти могла зробити своє замовлення максимально зручно та швидко!"),
			fmt.text(""),
			fmt.text("Поділись своїм номером , та обирай унікальний догляд, який можна підібрати для будь якого типу волосся, підкресливши твою індивідуальність 💙"),
			sep="\n"), parse_mode="HTML", reply_markup=shkb)
	await message.delete()

async def create_user(phone: str):
    conn = sqlite3.connect('users_num.db')
    cursor = conn.cursor()
    conn.execute('CREATE TABLE IF NOT EXISTS users(phone TEXT)')
    cursor.execute('INSERT OR IGNORE INTO users (phone) VALUES (?)', (phone,))
    conn.commit()
    conn.close()

async def contact_handler(message: types.Message):
	contact = message.contact
	await create_user(contact.phone_number)
	await bot.send_message(message.from_user.id,
		fmt.text(
			fmt.text("Ви успішно авторизувалися!"),
			fmt.text("Швидкий пошук товарів вже тут!"),
			sep="\n"), parse_mode="HTML", reply_markup=kb_client)

async def open_about(message : types.Message):
	await bot.send_message(message.from_user.id,
	 	fmt.text(
			fmt.text("Biosky - твій трендовий beauty-експерт із догляду за волоссям."),
			fmt.text(""),
			fmt.text("Італійський бренд професійної косметики для волосся в салонах України."),
			sep="\n"), parse_mode="HTML", reply_markup=kb_client)

async def menu_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Оберіть категорію товару:', reply_markup=in_kb)

async def kat_1(message : types.Message):
	await sqlite_db.kat1_read(message)
	await message.answer()

async def kat_2(message : types.Message):
	await sqlite_db.kat2_read(message)
	await message.answer()

async def kat_3(message : types.Message):
	await sqlite_db.kat3_read(message)
	await message.answer()

async def kat_4(message : types.Message):
	await sqlite_db.kat4_read(message)
	await message.answer()

async def kat_5(message : types.Message):
	await sqlite_db.kat5_read(message)
	await message.answer()

async def kat_6(message : types.Message):
	await sqlite_db.kat6_read(message)
	await message.answer()

async def kat_7(message : types.Message):
	await sqlite_db.kat7_read(message)
	await message.answer()

async def kat_8(message : types.Message):
	await sqlite_db.kat8_read(message)
	await message.answer()

async def kat_9(message : types.Message):
	await sqlite_db.kat9_read(message)
	await message.answer()

async def kat_10(message : types.Message):
	await sqlite_db.kat10_read(message)
	await message.answer()

async def kat_11(message : types.Message):
	await sqlite_db.kat11_read(message)
	await message.answer()

async def kat_12(message : types.Message):
	await sqlite_db.kat12_read(message)
	await message.answer()

async def kat_13(message : types.Message):
	await sqlite_db.kat13_read(message)
	await message.answer()

#async def menu_command(message : types.Message):
#	await sqlite_db.sql_read(message)


def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(command_start, commands=['start'])
	dp.register_message_handler(open_about, commands=['Головне'])
	dp.register_message_handler(menu_command, commands=['Каталог'])
	#dp.register_message_handler(private_office_handler, commands=['Відправити'])
	dp.register_message_handler(contact_handler, content_types=["contact"])
	dp.register_callback_query_handler(kat_1, lambda c: c.data == 'Kat1')
	dp.register_callback_query_handler(kat_2, lambda c: c.data == 'Kat2')
	dp.register_callback_query_handler(kat_3, lambda c: c.data == 'Kat3')
	dp.register_callback_query_handler(kat_4, lambda c: c.data == 'Kat4')
	dp.register_callback_query_handler(kat_5, lambda c: c.data == 'Kat5')
	dp.register_callback_query_handler(kat_6, lambda c: c.data == 'Kat6')
	dp.register_callback_query_handler(kat_7, lambda c: c.data == 'Kat7')
	dp.register_callback_query_handler(kat_8, lambda c: c.data == 'Kat8')
	dp.register_callback_query_handler(kat_9, lambda c: c.data == 'Kat9')
	dp.register_callback_query_handler(kat_10, lambda c: c.data == 'Kat10')
	dp.register_callback_query_handler(kat_11, lambda c: c.data == 'Kat11')
	dp.register_callback_query_handler(kat_12, lambda c: c.data == 'Kat12')
	dp.register_callback_query_handler(kat_13, lambda c: c.data == 'Kat13')
