from aiogram import Router, types
from aiogram.filters import Command

myinfo_router = Router()

@myinfo_router.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user_name = message.from_user.username
    if message.from_user.username is None:
        user_name = "Не указан"
    await message.answer(f"Ваш id: {user_id}\nимя:"
                         f" {name}\nник: {user_name}")
