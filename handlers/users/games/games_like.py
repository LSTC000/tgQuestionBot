from loader import dp

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.redis import GAME_NAME_REDIS_KEY

from database import update_game_likes, update_user_likes, update_user_n_game_dislike

from functions import update_user_n_game_like_cache, check_user_n_game_like_cache

from states import GamesStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA,
    state=GamesStatesGroup.finish_question
)
async def games_like(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Get game name from redis data.
    async with state.proxy() as data:
        game_name = data[GAME_NAME_REDIS_KEY]

    # Change value to user and game like.
    if not await check_user_n_game_like_cache(user_id=user_id, game_name=game_name):
        # Add 1 value to game likes.
        await update_game_likes(game_name)
        # Add 1 value to user likes.
        await update_user_likes(game_name)
        # Set True value to user and game like.
        await update_user_n_game_like_cache(
            user_id=user_id,
            game_name=game_name,
            value=True
        )
        # Set False value to user and game dislike.
        await update_user_n_game_dislike(
            user_id=user_id,
            game_name=game_name,
            value=False
        )
