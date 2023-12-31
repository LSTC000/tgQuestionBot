from loader import dp

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.config import GAMES_DATA

from data.redis import USER_ANSWERS_REDIS_KEY, GAME_QUESTION_NUMBER_REDIS_KEY, GAME_NAME_REDIS_KEY

from database import update_game_completed_attempts, update_user_completed_games, update_user_n_game_completed

from functions import clear_last_ikb, call_games_questions_creator, call_games_finish_creator

from states import GamesStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA, state=GamesStatesGroup.game_question)
async def games_creator(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    async with state.proxy() as data:
        # Add user answer in redis data.
        game_name = data[GAME_NAME_REDIS_KEY]
        question_number = data[GAME_QUESTION_NUMBER_REDIS_KEY]
        game_data = GAMES_DATA[game_name][0]
        questions = len(game_data)
        answers_data = game_data[question_number-1]['answers'][callback.data]
        finder_method = GAMES_DATA[game_name][1]['finder_method']

        if finder_method == 'best_weight':
            for key in answers_data:
                if str(key) not in data[USER_ANSWERS_REDIS_KEY]:
                    data[USER_ANSWERS_REDIS_KEY][str(key)] = 0
                data[USER_ANSWERS_REDIS_KEY][str(key)] += answers_data[key]

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Check whether this question is the last one.
    if question_number == questions:
        # Add 1 value to game completed attempts.
        await update_game_completed_attempts(game_name)
        # Add 1 value to user completed games.
        await update_user_completed_games(user_id)
        # Add 1 value to user and game completed.
        await update_user_n_game_completed(user_id=user_id, game_name=game_name)
        # Call finish creator.
        await call_games_finish_creator(user_id=user_id, state=state)
        # Set finish_question state.
        await GamesStatesGroup.finish_question.set()
    else:
        # Call questions creator.
        await call_games_questions_creator(user_id=user_id, state=state)
