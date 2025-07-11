# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp, bot
from utils import texts, buttons
from states.state import Feedback
from utils.env import GROUP_ID

@dp.message_handler(content_types=['text'], state=Feedback.feedback)
async def feedback(message: Message, state: FSMContext):
    feedback = message.text
    username = message.from_user.username or message.from_user.full_name
    user_id = message.from_user.id
    print(feedback)

    # Admin(ga) yuborish
    for group_id in GROUP_ID:
        try:
            await bot.send_message(
                chat_id=group_id,
                text=texts.send_feedback(username=username, feedback=feedback)
            )
        except Exception as e:
            print(f"Xatolik yuborishda: {group_id} -> {e}")

    # ✅ Foydalanuvchiga menyu yuborish
    await message.answer(
        texts.FEEDBACK_SUCCESS,
        reply_markup=buttons.send_menu_with_webapp(user_id)
    )

    # ✅ WebApp tugmasini alohida yuborish — `await` kerak emas!
    buttons.send_webapp_texts(user_id, texts.UNTEXT)

    await state.finish()