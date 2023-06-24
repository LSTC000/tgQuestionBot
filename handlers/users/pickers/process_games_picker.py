from loader import dp

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.redis import GAME_NAME_REDIS_KEY, GAME_QUESTION_REDIS_KEY, USER_ANSWERS_REDIS_KEY

from database import update_game_attempts

from functions import clear_last_ikb, clear_redis_data

from pickers import GamesPicker

from creators import GamesCreator

from states import PickersStatesGroup, GamesStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA, state=PickersStatesGroup.games_picker)
async def process_games_picker(callback: types.CallbackQuery, state: FSMContext) -> None:
    # Call process selection.
    pick, game_name = await GamesPicker().process_selection(
        callback=callback,
        callback_data=callback.data,
        state=state
    )
    # Check whether the user has made his choice.
    if pick:
        user_id = callback.from_user.id
        # Clear redis data.
        await clear_redis_data(state)
        # Add game name, point on first question and user answers in redis data.
        async with state.proxy() as data:
            data[GAME_NAME_REDIS_KEY] = game_name
            data[GAME_QUESTION_REDIS_KEY] = 0
            data[USER_ANSWERS_REDIS_KEY] = []
        # Add 1 value for the game attempts.
        await update_game_attempts(game_name)
        # Clear last inline keyboard.
        await clear_last_ikb(user_id=user_id, state=state)
        # Create a first game question.
        await GamesCreator().questions_creator(user_id=user_id, state=state)
        # Set game_question state.
        await GamesStatesGroup.game_question.set()
