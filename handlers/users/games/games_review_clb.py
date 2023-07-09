from loader import dp, bot

from data.callbacks import REVIEW_CALLBACK_DATA

from data.config import MAX_REVIEW_LENGTH

from data.messages import ENTER_GAME_REVIEW_MESSAGE

from states import GamesStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == REVIEW_CALLBACK_DATA, state=GamesStatesGroup.finish_question)
async def games_review_clb(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Please enter the user feedback.
    await bot.send_message(chat_id=user_id, text=ENTER_GAME_REVIEW_MESSAGE.format(MAX_REVIEW_LENGTH))
    # Set enter_review state.
    await GamesStatesGroup.enter_review.set()
