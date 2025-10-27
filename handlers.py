import os
from os import getenv

from aiogram import Router, F,Bot,Dispatcher
from aiogram.filters import CommandStart,Command
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
    user_email = State()
    kindle_email = State()
    wait_for_file=State()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(Reg.user_email)
    await message.answer('enter your email')


@router.message(Reg.user_email)
async def user_email(message: Message, state: FSMContext):
    await state.update_data(user_email=message.text)
    await state.set_state(Reg.kindle_email)
    await message.answer('enter your kindle  email')


@router.message(Reg.kindle_email)
async def kindle_email(message:Message, state: FSMContext):
    await state.update_data(kindle_email=message.text)
    data = await state.get_data()
    await message.answer(f'your user email is {data["user_email"]}\nyour kindle email is {data["kindle_email"]}')
    await  message.answer('send your file(no bigger then 20mb)')
    await state.set_state(Reg.wait_for_file)
@router.message(Reg.wait_for_file,F.document)
async def handle_file(message:Message):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, f"downloads/{message.document.file_name}")
    await message.answer(f'File downloaded {message.document.file_name}')
    os.remove(f'downloads/{message.document.file_name}')
    await message.answer(f'File deleted {message.document.file_name}')

