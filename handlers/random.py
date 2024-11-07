from aiogram import Router, types
from aiogram.filters import Command
from random import choice
random_router = Router()




@random_router.message(Command("random"))
async def random_handler(message: types.Message):
    ratatule = types.FSInputFile("images/ratatule.jpg")
    besh = types.FSInputFile("images/Besh.jpeg")
    omlette = types.FSInputFile("images/omlette.jpg")
    menu = [ratatule, besh, omlette]
    random_dish = choice(menu)
    if random_dish == ratatule:
        await message.answer_photo(
            photo=ratatule,
            caption="Рецепт:\n"
                    "кабачок — 2 шт. среднего размера;"
                    "баклажан — 1 шт.;\n"
                    "болгарский перец — 2 шт.;\n"
                    "помидор — 4 шт.;\n"
                    "репчатый лук — 2 головки;\n"
                    "чеснок — 4 зубчика;\n"
                    "томатная паста — 2 ст.л.;\n"
                    "вода — 100 мл;\n"
                    "растительное масло — 1 ст.л.;\n"
                    "соль, прованские травы — по вкусу.\n"

        )

    if random_dish == besh:
        await message.answer_photo(
            photo=besh,
            caption="Для приготовления лапши:"
                    " пшеничная мука в/с — 1,5 стакана, яйцо куриное — 1 шт.,\n"
                    " соль — 2 щепотки, фильтрованная вода — 2 ст. л.. 1\n"
                    "Для приготовления бульона: \n"
                    "говядина — 1,5–2 кг, лук репчатый — 1 шт.,\n"
                    " морковь — 1 шт., петрушка (стебли) — по вкусу,\n"
                    " соль — по вкусу. 1\n"
                    "Для подачи: жареный лук, зелень укропа. 1"
        )

    if random_dish == omlette:
        await message.answer_photo(
            photo=omlette,
            caption="куриное яйцо — 4 штуки;\n"
                    "молоко — 120 мл;\n"
                    "соль — щепотка;\n"
                    "растительное масло — 1 столовая ложка."
        )