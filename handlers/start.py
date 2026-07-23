from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from texts import START
from keyboards import main_keyboard


router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(START, reply_markup=main_keyboard)