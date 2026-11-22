
import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN topilmadi!")


dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ℹ️ Info"),
            KeyboardButton(text="📞 Contact")
        ],
        [
            KeyboardButton(text="👤 About"),
            KeyboardButton(text="📚 Courses")
        ],
    ],
    resize_keyboard=True
)


# START COMMAND
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Assalomu alaykum! Botimizga xush kelibsiz!",
        reply_markup=main_keyboard
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
        "Bu mening Python va aiogram yordamida\n"
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


# COURSE BUTTON HANDLER
@dp.message(F.text == "📚 Courses")
async def course_button_handler(message: Message):
    await message.answer(
        "Bizning kurslarimiz",
        reply_markup=main_keyboard
    )

# CONTACT BUTTON HANDLER
@dp.message(F.text == "📞 Contact")
async def contact_button_handler(message: Message):
    await message.answer(
    "Biz bilan bog'lanish",
    reply_markup=main_keyboard
)

# INFO BUTTON HANDLER
@dp.message(F.text == "ℹ️ Info")
async def info_button_handler(message: Message):
    await message.answer(
    "Bot nomi: My Python Bot\n"
    "Dasturlash tili: Python\n"
    "Framework: Aiogram\n"
    "Versiya: 1.0",
        reply_markup=main_keyboard
)

# ABOUT BUTTON HANDLER
@dp.message(F.text == "👤 About")
async def about_button_handler(message: Message):
    await message.answer(
       "Bu mening Python va aiogram yordamida\n"
               "yaratgan birinchi Telegram botim!",
        reply_markup=main_keyboard
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
