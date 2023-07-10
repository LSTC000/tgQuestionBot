from loader import dp, bot

from data.callbacks import DISLIKE_CALLBACK_DATA

from data.messages import SUCCESSFUL_SAVE_TEST_DISLIKE_MESSAGE, ERROR_SAVE_TEST_DISLIKE_MESSAGE

from data.redis import TEST_NAME_REDIS_KEY

from database import update_test_dislikes, update_user_dislikes

from functions import (
    update_user_n_test_like_cache,
    update_user_n_test_dislike_cache,
    check_user_n_test_like_cache,
    check_user_n_test_dislike_cache
)

from states import TestsStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == DISLIKE_CALLBACK_DATA,
    state=TestsStatesGroup.finish_question
)
async def tests_dislike(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Get test name from redis data.
    async with state.proxy() as data:
        test_name = data[TEST_NAME_REDIS_KEY]

    if not await check_user_n_test_dislike_cache(user_id=user_id, test_name=test_name):
        # Add 1 value to test dislikes.
        await update_test_dislikes(test_name)
        # Add 1 value to user dislikes.
        await update_user_dislikes(user_id)
        # Set True value to user and test dislike.
        await update_user_n_test_dislike_cache(user_id=user_id, test_name=test_name, value=True)

        if await check_user_n_test_like_cache(user_id=user_id, test_name=test_name):
            # Set False value to user and test like.
            await update_user_n_test_like_cache(user_id=user_id, test_name=test_name, value=False)

        await bot.send_message(chat_id=user_id, text=SUCCESSFUL_SAVE_TEST_DISLIKE_MESSAGE)
    else:
        await bot.send_message(chat_id=user_id, text=ERROR_SAVE_TEST_DISLIKE_MESSAGE)
