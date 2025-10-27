from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='button1'),KeyboardButton(text='button2'), KeyboardButton(text='button3')]],
    # изменили размер кнопок
    resize_keyboard=True,
    # добавили как бы строку-подсказку
    input_field_placeholder='choose option')