import asyncio

from aiogram import types
from aiogram.filters import CommandStart

from handlers.users.scarper import detect_alphabet, translate_text
from loader import dp, bot

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")

@dp.message()
async def start_handler(message: types.Message):
    text = detect_alphabet(message.text)
    pass