from loader import dp

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.config import GAMES_DATA

from data.redis import (
    USER_ANSWERS_REDIS_KEY,
    GAME_QUESTION_REDIS_KEY,
    GAME_QUESTION_NUMBER_REDIS_KEY,
    GAME_NAME_REDIS_KEY
)

from functions import clear_last_ikb, call_questions_creator

from states import GamesStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA, state=GamesStatesGroup.game_question)
async def questions_creator(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    async with state.proxy() as data:
        # Add user answer in redis data.
        data[USER_ANSWERS_REDIS_KEY].append((data[GAME_QUESTION_REDIS_KEY], callback.data))
        # Clear last inline keyboard.
        await clear_last_ikb(user_id=user_id, state=state)
        # Check whether this question is the last one.
        if data[GAME_QUESTION_NUMBER_REDIS_KEY] == len(GAMES_DATA[data[GAME_NAME_REDIS_KEY]]):
            #Set finish_question state.
            await GamesStatesGroup.finish_question.set()
        else:
            # Let's move on to the next question.
            data[GAME_QUESTION_NUMBER_REDIS_KEY] += 1
            # Call questions creator.
            await call_questions_creator(user_id=user_id, state=state)
