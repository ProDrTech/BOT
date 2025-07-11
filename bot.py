from aiogram import executor
from loader import bot, dp
from utils.env import ADMIN
from utils.webapp import set_webapp_button
from data.config import check_provider_tokens
import handlers  # bu yerda barcha handlerlar yuklanadi

async def on_startup(dp):
    """
    Botni ishga tushiradi
    """
    print("Bot ishga tushmoqda...")
    for admin_id in ADMIN:
        try:
            await bot.send_message(admin_id, "✅ Bot ishga tushdi")
        except Exception as e:
            print(f"❌ Xatolik admin {admin_id} ga yuborishda: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
