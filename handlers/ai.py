# handlers/ai.py
from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.state import AIChat
from services import ask_gemini
from utils import buttons, texts
from utils.buttons import BACK

@dp.message_handler(text='AI bilan suhbat', state='*')
async def start_ai_chat(message: types.Message, state: FSMContext):
    await message.answer("🤖 AI yordamchi bilan suhbatni boshladingiz.\nSavolingizni yozing...", reply_markup=BACK)
    await AIChat.chatting.set()

@dp.message_handler(text='⬅️ Ortga', state=AIChat.chatting)
async def stop_ai_chat(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await message.answer("🏠 Asosiy menyuga qaytdingiz.", reply_markup=buttons.send_menu_with_webapp(user_id))
    buttons.send_webapp_texts(user_id, texts.UNTEXT)
    await state.finish()

@dp.message_handler(state=AIChat.chatting)
async def handle_ai_messages(message: types.Message, state: FSMContext):
    waiting_msg = await message.answer("⏳ AI yordamchi javob yozmoqda...")

    javob = await ask_gemini(message.text)

    await message.bot.delete_message(chat_id=message.chat.id, message_id=waiting_msg.message_id)

    await message.answer(javob)
