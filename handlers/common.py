from aiogram import Router
from aiogram.types import Message

from texts import UNKNOWN

router = Router()

@router.message()
async def unknown_message_handler(message: Message):
    await message.answer(UNKNOWN)