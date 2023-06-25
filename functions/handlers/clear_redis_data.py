from data.redis import (
    PICKER_PAGE_REDIS_KEY,
    GAME_NAME_REDIS_KEY,
    GAME_QUESTION_REDIS_KEY,
    GAME_QUESTION_NUMBER_REDIS_KEY,
    TEST_NAME_REDIS_KEY,
    TEST_QUESTION_NUMBER_REDIS_KEY,
    USER_ANSWERS_REDIS_KEY
)

from aiogram.dispatcher.storage import FSMContext


async def clear_redis_data(state: FSMContext) -> None:
    '''
    :param state: FSMContext.
    :return: None.
    '''

    async with state.proxy() as data:
        if PICKER_PAGE_REDIS_KEY in data:
            data.pop(PICKER_PAGE_REDIS_KEY)

        if GAME_NAME_REDIS_KEY in data:
            data.pop(GAME_NAME_REDIS_KEY)

        if GAME_QUESTION_REDIS_KEY in data:
            data.pop(GAME_QUESTION_REDIS_KEY)

        if GAME_QUESTION_NUMBER_REDIS_KEY in data:
            data.pop(GAME_QUESTION_NUMBER_REDIS_KEY)

        if TEST_NAME_REDIS_KEY in data:
            data.pop(TEST_NAME_REDIS_KEY)

        if TEST_QUESTION_NUMBER_REDIS_KEY in data:
            data.pop(TEST_QUESTION_NUMBER_REDIS_KEY)

        if USER_ANSWERS_REDIS_KEY in data:
            data.pop(USER_ANSWERS_REDIS_KEY)
