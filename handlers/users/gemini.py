from aiogram import types
from loader import dp
from services import ask_gemini

@dp.message_handler(lambda message: message.text and not message.text.startswith("/"))
async def gemini_handler(message: types.Message):
    await message.answer("⏳ Javob yozilmoqda...")
    javob = await ask_gemini(message.text)
    await message.answer(javob)