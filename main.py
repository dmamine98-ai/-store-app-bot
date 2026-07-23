import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# ضع التوكن الخاص ببوتك هنا أو في متغيرات البيئة (Environment Variables) في Railway
TOKEN = "YOUR_BOT_TOKEN_HERE"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    هذا المعالج يتم تفعيله عند إرسال أمر /start للبوت
    """
    await message.answer(f"مرحباً بك يا {html.quote(message.from_user.full_name)}! تم تشغيل البوت بنجاح على المنصة.")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())