import os
from os import getenv

import dotenv

import sender

dotenv.load_dotenv()

from aiogram import Router, F, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv('BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

router = Router()


class Reg(StatesGroup):
    kindle_email = State()
    file = State()


@router.message(CommandStart())
async def get_kindle_email(message: Message, state: FSMContext):
    await state.set_state(Reg.kindle_email)
    await message.answer('enter your kindle  email')


@router.message(Reg.kindle_email)
async def kindle_email(message: Message, state: FSMContext):
    await state.update_data(kindle_email=message.text)
    await  message.answer('send your file(no bigger then 20mb)')
    await state.set_state(Reg.file)


@router.message(Reg.file, F.document)
async def handle_file(message: Message, state: FSMContext):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_name = message.document.file_name
    data = await  state.get_data()
    if not os.path.isdir('books'):
        os.mkdir('books')
    await bot.download_file(file_path, f"books/{message.document.file_name}")
    await message.answer(f'file received {message.document.file_name}')
    await sender.send_email(receiver_email=data['kindle_email'], filename=file_name)
    await message.answer(f'File sent {message.document.file_name}')
    await state.clear()
    os.remove(f'books/{file_name}')
    await message.answer(f'File deleted {file_name}')
    if os.path.isdir('books') and len(os.listdir('books')) == 0:
        os.rmdir('books')
        await message.answer('Folder deleted')


