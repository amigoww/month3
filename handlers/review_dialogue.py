from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


review_router = Router()

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

@review_router.callback_query(F.data == "review")
async def start_review(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await callback_query.message.answer("Как вас зовут?")


@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.phone_number)
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефона или инстаграм")


@review_router.message(RestourantReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Дата вашего визита")
    await state.update_data(phone_number=message.text)


@review_router.message(RestourantReview.visit_date)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.food_rating)

    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="плохо"),
                types.KeyboardButton(text="хорошо"),
                types.KeyboardButton(text="отлично")
            ]
        ]
    )
    await message.answer("Как оцениваете качество еды", reply_markup=kb)

    await state.update_data(visit_date=message.text)


@review_router.message(RestourantReview.food_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.cleanliness_rating)
    await message.answer("Как оцениваете чистоту заведения")

    await state.update_data(food_rating=message.text)


@review_router.message(RestourantReview.cleanliness_rating)
async def process_extra_comments(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    await state.set_state(RestourantReview.extra_comments)
    await message.answer("Дополнительные коментарии/Жалобы", reply_markup=kb)
    await state.update_data(cleanliness_rating=message.text)


@review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за отзыв!")
    await state.update_data(extra_comments=message.text)
    data = await state.get_data()
    print(data)
    await state.clear()