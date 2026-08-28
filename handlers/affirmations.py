from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from database import get_user_settings
from storage import load_affirmations, save_affirmations
from services import get_random_affirmation, get_all_affirmations_text, add_affirmation
from texts import EMPTY_ADD, SHORT_ADD, add_text_affirmation
from keyboards import again_affirmation_keyboard

router = Router()


async def send_random_affirmation(message: Message):
    user_id = message.from_user.id
    settings = get_user_settings(user_id)
    mode = settings["mode"]

    data = load_affirmations()
    text = get_random_affirmation(data, mode)

    await message.answer(text, reply_markup=again_affirmation_keyboard)


MAX_MESSAGE_LENGTH = 3500


def split_text(text, max_length=MAX_MESSAGE_LENGTH):
    parts = []
    current_part = ""

    for line in text.split("\n"):
        if len(current_part) + len(line) + 1 > max_length:
            parts.append(current_part)
            current_part = line
        else:
            if current_part:
                current_part += "\n"
            current_part += line

    if current_part:
        parts.append(current_part)

    return parts


async def send_all_affirmations(message: Message):
    user_id = message.from_user.id
    settings = get_user_settings(user_id)
    mode = settings["mode"]

    data = load_affirmations()
    text = get_all_affirmations_text(data, mode)

    for part in split_text(text):
        await message.answer(part)


@router.message(Command("affirmation"))
async def affirmation_handler(message: Message):
    await send_random_affirmation(message)


@router.message(F.text == "Получить аффирмацию")
async def affirmation_button_handler(message: Message):
    await send_random_affirmation(message)


@router.callback_query(F.data == "new_affirmation")
async def callback_affirmation(callback: CallbackQuery):
    user_id = callback.from_user.id
    settings = get_user_settings(user_id)
    mode = settings["mode"]

    data = load_affirmations()
    text = get_random_affirmation(data, mode)

    await callback.message.answer(text, reply_markup=again_affirmation_keyboard)
    await callback.answer()


@router.message(Command("all"))
async def all_handler(message: Message):
    await send_all_affirmations(message)


@router.message(F.text == "Все аффирмации")
async def all_button_handler(message: Message):
    await send_all_affirmations(message)


@router.message(Command("add"))
async def add_handler(message: Message):
    if message.text.strip() == "/add":
        await message.answer(EMPTY_ADD)
        return

    new_affirmation = message.text.replace("/add", "", 1).strip()

    if len(new_affirmation) < 3:
        await message.answer(SHORT_ADD)
        return

    user_id = message.from_user.id
    settings = get_user_settings(user_id)
    mode = settings["mode"]

    data = load_affirmations()
    add_affirmation(data, mode, new_affirmation)
    save_affirmations(data)

    await message.answer(add_text_affirmation(new_affirmation))