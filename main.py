import asyncio

import logging
from bot_config import bot, dp, database
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random import random_router
from handlers.other_messages import echo_router
from handlers.review_dialogue import review_router

async def on_startup(bot):
    database.create_tables()
    # await bot.send_message(chat_id=12321312,text="я онлан")


async def main():
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(random_router)
    dp.include_router(review_router)

    # в самом конце
    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    #запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())