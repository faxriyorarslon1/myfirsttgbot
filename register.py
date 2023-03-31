import logging
from aiogram import Bot, Dispatcher, executor, types
import buttons
import matnlar
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Text

API_TOKEN = '6297078799:AAHa4p_m3PURpeqhoVuj7Hrewa-QgsfEuGI'

user_data = {}

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id, matnlar.welcome_text, reply_markup=buttons.welcome_keyboard, parse_mode = ParseMode.MARKDOWN)

@dp.message_handler(Text(equals=["Bizning Kurslarimiz", "Biz bilan aloqa"]))
async def course_or_contact(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    if text == "Bizning Kurslarimiz":
        await bot.send_message(user_id, matnlar.our_course_text, reply_markup = buttons.our_courses, parse_mode = ParseMode.MARKDOWN)
    else:
        await bot.send_message(user_id, "Hali bu qism test jarayonida")


@dp.message_handler(Text(equals=["Ingliz tili", "Rus tili", "Arab tili", "Koreys tili"]))
async def about_courses(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    if text == "Ingliz tili":
        msg_txt = matnlar.about_english
    elif text == "Rus tili":
       msg_txt = matnlar.about_russian
    elif text == "Arab tili":
       msg_txt = matnlar.about_arabic
    else:
        msg_txt = matnlar.about_korean
    await bot.send_message(user_id, msg_txt, reply_markup = buttons.register_to_course, parse_mode = ParseMode.MARKDOWN)

@dp.message_handler(content_types=['text'])
async def register_course(message: types.Message):
    user_id = message.from_user.id
    step = user_data[user_id]["step"]
    if step == "name":
        user_data[user_id]["name"] = message.text
        print(user_data[user_id])
        await bot.send_message(user_id, "Iltimos telefon raqamingizni yuboring: ")
        user_data[user_id]["step"] = "phone"
    elif step == "phone":
        user_data[user_id]["phone"] = message.text
        print(user_data[user_id])
        await bot.send_message(user_id, "Sizga darslar uchun qaysi vaqt qulay ekanligini yozing:")
        


@dp.callback_query_handler()
async def callbacks_num(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer("Biz sizni o'qitishdan mamnunmiz !!!")
    await bot.send_message(user_id, "Iltimos ismingizni yuboring: ")
    user_data[user_id] = {}
    user_data[user_id]["step"] = "name"

    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)