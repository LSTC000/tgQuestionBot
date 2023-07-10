from loader import dp, bot

from data.callbacks import REVIEW_CALLBACK_DATA

from data.config import MAX_REVIEW_LENGTH

from data.messages import ENTER_TEST_REVIEW_MESSAGE

from states import TestsStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == REVIEW_CALLBACK_DATA, state=TestsStatesGroup.finish_question)
async def tests_review_clb(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Please enter the user feedback.
    await bot.send_message(chat_id=user_id, text=ENTER_TEST_REVIEW_MESSAGE.format(MAX_REVIEW_LENGTH))
    # Set enter_review state.
    await TestsStatesGroup.enter_review.set()
