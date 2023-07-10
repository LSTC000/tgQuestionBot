from loader import dp, bot

from data.config import MAX_REVIEW_LENGTH

from data.messages import SUCCESSFUL_SAVE_TEST_REVIEW_MESSAGE, ERROR_SAVE_TEST_REVIEW_MESSAGE

from data.redis import TEST_NAME_REDIS_KEY

from database import add_user_review

from states import TestsStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(state=TestsStatesGroup.enter_review)
async def tests_review_msg(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    text = message.text

    # Check review length.
    if len(text) <= MAX_REVIEW_LENGTH:
        async with state.proxy() as data:
            test_name = data[TEST_NAME_REDIS_KEY]
        # Add review about the test in database.
        await add_user_review(user_id=user_id, target='test', target_name=test_name, review=text)
        # Inform the user about successful save review.
        await bot.send_message(chat_id=user_id, text=SUCCESSFUL_SAVE_TEST_REVIEW_MESSAGE)
    else:
        # Inform the user about error save review.
        await bot.send_message(chat_id=user_id, text=ERROR_SAVE_TEST_REVIEW_MESSAGE.format(MAX_REVIEW_LENGTH))

    # Set finish_question state.
    await TestsStatesGroup.finish_question.set()
