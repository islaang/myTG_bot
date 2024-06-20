from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile, KeyboardButton, ReplyKeyboardMarkup
from parcingmain import *

router = Router()
@router.message(CommandStart())
async def start(message:Message):
    description = (
        "Привет, я бот помощник! \n"
        "Этот бот предназначен для парсинга сайта отеля \n"
        "Ты можешь выбрать данные про отели, какие только пожелаешь!\n"
        "Используй эти кнопки!"
    )
    kb = [
        [KeyboardButton(text="Вывести цену")],
        [KeyboardButton(text="Вывести название")],
        [KeyboardButton(text="hello")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb,resize_keyboard=True)
    await message.answer(description, reply_markup=keyboard)


# @router.message(F.text == 'Вывести цену')
# async def price(message:Message):
#     await message.answer(get_price)

# @router.message(F.text == 'Вывести название')
# async def name(message:Message):
#     await message.answer(get_)