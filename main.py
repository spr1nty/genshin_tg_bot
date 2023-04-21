from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/start</b> - <em>Начало работы бота.</em>
<b>/help</b> - <em>Список команд.</em>
<b>/description</b> - <em>Описание бота.</em>
"""

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/description')
b3 = KeyboardButton(text='Альбедо')
b4 = KeyboardButton(text='Барбара')
b5 = KeyboardButton(text='Беннет')
b6 = KeyboardButton(text='Бей Доу')
b7 = KeyboardButton(text='Венти')
b8 = KeyboardButton(text='Гань Юй')
b9 = KeyboardButton(text='Джинн')
b10 = KeyboardButton(text='Дилюк')
b11 = KeyboardButton(text='Диона')
b12 = KeyboardButton(text='Кли')
b13 = KeyboardButton(text='Кэ цин')
b14 = KeyboardButton(text='Кэйа')
#b15 = KeyboardButton(text='Кли')
#b16 = KeyboardButton(text='Кли')
#b17 = KeyboardButton(text='Кли')

kb.add(b1)
kb.add(b2)
kb.add(b3)
kb.add(b4)
kb.add(b5)
kb.add(b6)
kb.add(b7)
kb.add(b8)
kb.add(b9)
kb.add(b10)
kb.add(b11)
kb.add(b12)
kb.add(b13)
kb.add(b14)

async def on_startup(_):
    print('Успешно.')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать в нашего бота,/n здесь вы можете получить помощь по прокачке своих персонажей и не только(пока что толькоько персонажей)!",
                           reply_markup=kb)

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Наш бот идеален.',
                           reply_markup=kb)# !!!
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           parse_mode='HTML',
                           text=HELP_COMMAND,
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(text='Альбедо')
async def albedos_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-1-1024x576.jpg')

@dp.message_handler(text='Барбара')
async def bar_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-2-1024x576.jpg')

@dp.message_handler(text='Беннет')
async def ben_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-3-1024x576.jpg')

@dp.message_handler(text='Бей Доу')
async def bei_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-4-1024x576.jpg')

@dp.message_handler(text='Венти')
async def ven_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-5-1024x576.jpg')

@dp.message_handler(text='Гань Юй')
async def gan_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-6-1024x576.jpg')

@dp.message_handler(text='Джинн')
async def jinn_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-7-1024x576.jpg')

@dp.message_handler(text='Дилюк')
async def dil_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-8-1024x576.jpg')

@dp.message_handler(text='Диона')
async def dio_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-9-1024x576.jpg')

@dp.message_handler(text='Кли')
async def kli_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-10-1024x576.jpg')

@dp.message_handler(text='Кэ цин')
async def kez_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-11-1024x576.jpg')

@dp.message_handler(text='Кэйа')
async def keya_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-12-1024x576.jpg')

#@dp.message_handler(text='albedo')
#async def albedos_command(message: types.Message):
    #await bot.send_photo(chat_id=message.from_user.id,
                        # photo='https://genshindb.ru/wp-content/uploads/2021/07/Vozvishenie-pers-gyde-13-1024x576.jpg')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)
