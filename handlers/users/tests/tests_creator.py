from loader import dp

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.config import TESTS_DATA

from data.redis import USER_ANSWERS_REDIS_KEY, TEST_QUESTION_NUMBER_REDIS_KEY, TEST_NAME_REDIS_KEY

from database import update_test_completed_attempts, update_user_completed_tests, update_user_n_test_completed

from functions import clear_last_ikb, call_tests_questions_creator, call_tests_finish_creator

from states import TestsStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA, state=TestsStatesGroup.test_question)
async def tests_creator(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    async with state.proxy() as data:
        # Add user answer in redis data.
        test_name = data[TEST_NAME_REDIS_KEY]
        question_number = data[TEST_QUESTION_NUMBER_REDIS_KEY]
        test_data = TESTS_DATA[test_name][0]
        questions = len(test_data)
        answers_data = test_data[question_number-1]['answers'][callback.data]
        finder_method = TESTS_DATA[test_name][1]['finder_method']

        if finder_method == 'best_weight':
            for key in answers_data:
                if str(key) not in data[USER_ANSWERS_REDIS_KEY]:
                    data[USER_ANSWERS_REDIS_KEY][str(key)] = 0
                data[USER_ANSWERS_REDIS_KEY][str(key)] += answers_data[key]

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Check whether this question is the last one.
    if question_number == questions:
        # Add 1 value to test completed attempts.
        await update_test_completed_attempts(test_name)
        # Add 1 value to user completed tests.
        await update_user_completed_tests(user_id)
        # Add 1 value to user and test completed.
        await update_user_n_test_completed(user_id=user_id, test_name=test_name)
        # Call finish creator.
        await call_tests_finish_creator(user_id=user_id, state=state)
        # Set finish_question state.
        await TestsStatesGroup.finish_question.set()
    else:
        # Call questions creator.
        await call_tests_questions_creator(user_id=user_id, state=state)
