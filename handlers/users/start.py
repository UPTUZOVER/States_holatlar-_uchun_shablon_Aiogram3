from aiogram.filters import CommandStart
from loader import dp
from aiogram import types
@dp.message(CommandStart())
async def start_bot(message:types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!")
