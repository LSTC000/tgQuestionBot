from loader import dp

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.redis import TEST_NAME_REDIS_KEY, TEST_QUESTION_NUMBER_REDIS_KEY, USER_ANSWERS_REDIS_KEY

from database import update_test_attempts, update_user_opened_tests, update_user_n_test_opened, add_user_n_test

from functions import (
    clear_last_ikb,
    clear_redis_data,
    call_tests_questions_creator,
    check_user_n_test_cache,
)

from pickers import TestsPicker

from states import PickersStatesGroup, TestsStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA, state=PickersStatesGroup.tests_picker)
async def process_tests_picker(callback: types.CallbackQuery, state: FSMContext) -> None:
    # Call process selection.
    pick, test_name = await TestsPicker().process_selection(
        callback=callback,
        callback_data=callback.data,
        state=state
    )
    # Check whether the user has made his choice.
    if pick:
        user_id = callback.from_user.id
        # Clear redis data.
        await clear_redis_data(state)
        # Add test name, point on first question and user answers in redis data.
        async with state.proxy() as data:
            data[TEST_NAME_REDIS_KEY] = test_name
            data[TEST_QUESTION_NUMBER_REDIS_KEY] = 0
            data[USER_ANSWERS_REDIS_KEY] = {}
        # Add 1 value for the test attempts.
        await update_test_attempts(test_name)
        # Add 1 value for the user opened tests.
        await update_user_opened_tests(user_id)
        # Check user and test in database and cache.
        if not await check_user_n_test_cache(user_id=user_id, test_name=test_name):
            await add_user_n_test(user_id=user_id, test_name=test_name)
        # Add 1 value for the user and test opened.
        await update_user_n_test_opened(user_id=user_id, test_name=test_name)
        # Clear last inline keyboard.
        await clear_last_ikb(user_id=user_id, state=state)
        # Call a first game question.
        await call_tests_questions_creator(user_id=user_id, state=state)
        # Set game_question state.
        await TestsStatesGroup.test_question.set()
