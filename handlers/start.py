# aiogram import
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

# kode import
from loader import dp
from utils import texts, buttons
from services import getUser
from states.state import Register
from .menu import Menu
from utils.webapp import set_webapp_button
from aiogram.types import CallbackQuery
import aiohttp
from loader import dp, bot

SUBSCRIBE_API_URL = "https://asadmaxmud.up.railway.app/api/v1/subscribe/"

@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id

    # 1. Avval user ro‘yxatdan o‘tganmi — tekshirib olamiz
    user = getUser(user_id)
    if user:
        # WebApp tugmasi qo‘shish (agar kerak bo‘lsa)
        set_webapp_button("https://frontend-six-zeta-98.vercel.app/", chat_id=user_id)

        # To‘g‘ridan-to‘g‘ri menu
        await Menu(message, state)
        return

    # 2. Kanalga obuna bo‘lganini tekshirish uchun API’dan linklar olib kelamiz
    async with aiohttp.ClientSession() as session:
        async with session.get(SUBSCRIBE_API_URL) as resp:
            data = await resp.json()

    telegram_links = [item for item in data if item['platform'] == 'telegram']
    other_links = [item for item in data if item['platform'] != 'telegram']

    if telegram_links or other_links:
        buttons = [
            [types.InlineKeyboardButton(text=link['name'], url=link['url'])]
            for link in telegram_links + other_links
        ]
        buttons.append([types.InlineKeyboardButton(text="✅ Tekshirdim", callback_data="check_sub")])

        await message.answer(
            "Iltimos, quyidagi kanallarga obuna bo‘ling 👇",
            reply_markup=types.InlineKeyboardMarkup(inline_keyboard=buttons)
        )
        return

    # Agar obuna qilish majburiy bo‘lmasa va user ham ro‘yxatdan o‘tmagan bo‘lsa
    set_webapp_button("https://frontend-six-zeta-98.vercel.app/", chat_id=user_id)

    await message.answer(texts.REGISTER_FULLNAME)
    await Register.name.set()

@dp.callback_query_handler(lambda c: c.data == "check_sub")
async def check_subscription_status(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id

    # API orqali kanallarni olish
    async with aiohttp.ClientSession() as session:
        async with session.get(SUBSCRIBE_API_URL) as resp:
            data = await resp.json()

    telegram_channels = [item for item in data if item['platform'] == 'telegram']
    failed = []

    # Har bir kanal bo‘yicha obuna holatini tekshirish
    for ch in telegram_channels:
        try:
            member = await bot.get_chat_member(chat_id=f"@{ch['channel_username']}", user_id=user_id)
            if member.status not in ['member', 'administrator', 'creator']:
                failed.append(ch['name'])
        except Exception as e:
            failed.append(ch['name'])

    # Agar obuna bo‘lmagan kanal bo‘lsa — alert chiqarish
    if failed:
        await call.answer("❌ Obuna bo‘lmagan kanal(lar): " + ", ".join(failed), show_alert=True)
    else:
        await call.message.delete()

        # 1. Obuna muvaffaqiyatli bo‘ldi degan xabar
        await call.message.answer("✅ Obunalar tasdiqlandi.\nSiz botdan to‘liq foydalanishingiz mumkin")

        # 2. Keyin ism so‘ralsin
        await call.message.answer("Ismingizni kiriting:")
        await Register.name.set()
        
