from loader import dp, bot

from data.messages import SUCCESSFUL_SAVE_GAME_REVIEW_MESSAGE

from data.redis import GAME_NAME_REDIS_KEY

from database import add_user_review

from states import GamesStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(state=GamesStatesGroup.enter_review)
async def games_review_msg(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    async with state.proxy() as data:
        game_name = data[GAME_NAME_REDIS_KEY]

    # Add review about the game in database.
    await add_user_review(user_id=user_id, target='game', target_name=game_name, review=message.text)
    # Inform the user about successful save review.
    await bot.send_message(chat_id=user_id, text=SUCCESSFUL_SAVE_GAME_REVIEW_MESSAGE)
    # Set finish_question state.
    await GamesStatesGroup.finish_question.set()