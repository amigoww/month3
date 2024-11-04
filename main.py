import asyncio
import random


from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values

token = dotenv_values(".env").get("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()

names = ["Amir", "Kairat", "Azamat", "Nigina", "Daulet", "Churok"]

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    msg = f"Привет {name}"
    await message.answer(msg)

@dp.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username
    if message.from_user.username is None:
        user_name = "Не указан"
    await message.answer(f"Ваш id: {user_id}\nимя: {name}\nник: {user_name}")

@dp.message(Command("random"))
async def random_handler(message: types.Message):
    random_name = random.choice(names)
    await message.answer(f"Случайное имя: {random_name}")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())