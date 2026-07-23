from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from database import get_user_settings, set_user_enabled, set_user_time
from keyboards import settings_keyboard

router = Router()

def make_text_settings(settings):
    status = "включена" if settings["enabled"] else "выключена"
    return f"""Твои настройки:
Ежедневная аффирмация: {status}
Время: {settings["time"]}"""

async def show_settings(message: Message):
    user_id = message.from_user.id
    settings = get_user_settings(user_id)
    text = make_text_settings(settings)
    await message.answer(text, reply_markup=settings_keyboard)


@router.message(Command("settings"))
async def settings_handler(message: Message):
    await show_settings(message)

@router.message(F.text == "Настройки")
async def settings_button_handler(message: Message):
    await show_settings(message)


@router.message(Command("on"))
async def on_handler(message: Message):
    user_id = message.from_user.id
    set_user_enabled(user_id, True)
    await message.answer("Ежедневная аффирмация включена")

@router.callback_query(F.data == "settings_on")
async def settings_on_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    set_user_enabled(user_id, True)
    settings = get_user_settings(user_id)
    text = make_text_settings(settings)
    await callback.message.edit_text(text, reply_markup=settings_keyboard)
    await callback.answer()

@router.message(Command("off"))
async def off_handler(message: Message):
    user_id = message.from_user.id
    set_user_enabled(user_id, False)
    await message.answer("Ежедневная аффирмация выключена")

@router.callback_query(F.data == "settings_off")
async def settings_off_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    set_user_enabled(user_id, False)
    settings = get_user_settings(user_id)
    text = make_text_settings(settings)
    await callback.message.edit_text(text, reply_markup=settings_keyboard)
    await callback.answer()


@router.message(Command("settime"))
async def settime_handler(message: Message):
    user_id = message.from_user.id
    new_time = message.text.replace("/settime", "", 1).strip()
    if len(new_time) != 5 or new_time[2] != ":":
        await message.answer("Неверное время. Напиши время так: /settime 09:00")
        return
    hours = new_time[:2]
    minutes = new_time[3:]
    if not hours.isdigit() or not minutes.isdigit():
        await message.answer("Неверное время. Напиши время так: /settime 09:00")
        return
    hours_number = int(hours)
    minutes_number = int(minutes)
    if not (0 <= hours_number <= 23 and 0 <= minutes_number <= 59):
        await message.answer("Неверное время. Напиши время так: /settime 09:00")
        return
    set_user_time(user_id, new_time)
    settings = get_user_settings(user_id)
    text = make_text_settings(settings)
    await message.answer(text, reply_markup=settings_keyboard)

    
