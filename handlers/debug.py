from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from config import ADMIN_ID
from database import get_all_users

router = Router()

@router.message(Command("debug_users"))
async def debug_users_handler(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("У тебя нет доступа к этой команде")
        return
    
    rows = get_all_users()
    if not rows:
        await message.answer("Пользователей пока нет")
        return
    text = "Пользователи в базе:\n\n"
    for user_id, enabled, time, last_sent_date in rows:
        status = "включена" if enabled else "выключена"
        text += f"Пользователь: {user_id}, ежедневная аффирмация: {status}, время: {time}, последняя отправка: {last_sent_date}\n"
    await message.answer(text)

