import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6297078799:AAHa4p_m3PURpeqhoVuj7Hrewa-QgsfEuGI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Hi { message.from_user.first_name }!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(content_types=['text'])
async def alik_ol(message: types.Message):
    if message.text == "Salom":
        await message.reply("va aleykum assalom")
    else:
        await message.reply("Sizga qanday yordam bera olaman")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


#o'quv markazi uchun ro'yxatga oluvchi bot
# ism familya so'raladi
# telefon raqam so'raladi
# qaysi kursga qatnashmoqchi ekanligi so'raladi
# qaysi vaqt u uchun qulay ekanligi so'raladi    