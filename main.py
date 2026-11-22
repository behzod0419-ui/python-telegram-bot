
import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN topilmadi!")


dp = Dispatcher()


# START COMMAND
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Assalomu alaykum! Botimizga xush kelibsiz!"
    )


# HELP COMMAND
@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Yordam bo'limi:\n"
        "/start - Botni boshlash\n"
        "/help - Yordam\n"
        "/about - Bot haqida\n"
        "/info - Info haqida"
    )


# ABOUT COMMAND
@dp.message(Command("about"))
async def about_handler(message: Message):
    await message.answer(
        "Bu mening Python va aiogram yordamida "
        "yaratgan birinchi Telegram botim!"
    )


# INFO COMMAND
@dp.message(Command("info"))
async def info_handler(message: Message):
    await message.answer(
    "Bot nomi: My Python Bot\n"
    "Dasturlash tili: Python\n"
    "Framework: Aiogram\n"
    "Versiya: 1.0"
)


# TEXT MESSAGE HANDLER
@dp.message(F.text)
async def message_handler(message: Message):
    await message.answer(
        f"Siz yozdingiz: {message.text}"
    )


async def main():
    bot = Bot(token=BOT_TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
