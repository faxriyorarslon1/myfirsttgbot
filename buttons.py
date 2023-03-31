from aiogram import types

welcome_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Bizning Kurslarimiz")
button2 = types.KeyboardButton("Biz bilan aloqa")
welcome_keyboard.add(button1, button2)


our_courses = types.ReplyKeyboardMarkup(resize_keyboard=True)
course1 = types.KeyboardButton("Ingliz tili")
course2 = types.KeyboardButton("Rus tili")
course3 = types.KeyboardButton("Arab tili")
course4 = types.KeyboardButton("Koreys tili")
#our_course.add(course1)
our_courses.add(course1, course2)
our_courses.add(course3, course4)

register_to_course = types.InlineKeyboardMarkup(resize_keyboard=True)
reg_button = types.InlineKeyboardButton("Kursga ro'yxatdan o'tish",callback_data="register_course")
register_to_course.add(reg_button)
