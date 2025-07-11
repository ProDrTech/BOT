# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# project import
from loader import dp, bot
from utils import texts, buttons
from states.state import Collobration
from utils.env import ADMIN

from asyncio import create_task


async def info_task(message: Message, state: FSMContext):
    username = message.from_user.username or message.from_user.first_name

    data = await state.get_data()
    name = data.get('name')
    phone = data.get('phone')
    location = data.get('location')

    info = message.text
    await state.update_data({'info': info})

    caption = texts.collaboration(
        name=name,
        phone=phone,
        username=username,
        location=location,
        info=info
    )

    # Barcha adminlarga xabar yuborish
    for admin_id in ADMIN:
        try:
            await bot.send_message(chat_id=admin_id, text=caption)
        except Exception as e:
            print(f"Xatolik admin {admin_id} ga yuborishda: {e}")

    await message.answer(texts.SUCCESS_COLLABORATION, reply_markup=buttons.MAIN_BACK)

    user_id = message.from_user.id
    text = texts.UNTEXT
    # Agar send_webapp_texts async bo'lsa:
    # await buttons.send_webapp_texts(user_id, text)
    buttons.send_webapp_texts(user_id, text)

    await state.finish()


@dp.message_handler(content_types=['text'], state=Collobration.info)
async def info(message: Message, state: FSMContext):
    if message.text in [buttons.BACK_TEXT]:
        await message.answer(texts.LOCATION, reply_markup=buttons.BACK)
        await Collobration.location.set()
    else:
        await create_task(info_task(message, state))
