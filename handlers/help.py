from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from texts import HELP


router = Router()


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(HELP)


@router.message(F.text == "Помощь")
async def help_button_handler(message: Message):
    await message.answer(HELP)