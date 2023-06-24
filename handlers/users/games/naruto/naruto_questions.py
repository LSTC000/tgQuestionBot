from loader import dp

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.redis import USER_ANSWERS_REDIS_KEY

from creators import GamesCreator

from states import GamesStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA, state=GamesStatesGroup.game_question)
async def naruto_questions(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Add user answer un redis data.
    async with state.proxy() as data:
        data[USER_ANSWERS_REDIS_KEY].append(callback.data)
    # Call next question.
    await GamesCreator.questions_creator(user_id=callback.from_user.id, state=state)
