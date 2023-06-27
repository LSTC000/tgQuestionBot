from data.redis import (
    GAME_QUESTION_REDIS_KEY,
    GAME_QUESTION_NUMBER_REDIS_KEY,
    LAST_IKB_REDIS_KEY,
)

from creators import GamesCreator

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_games_questions_creator(user_id: int, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Get image, question and questions inline keyboard.
        image, question, ikb = await GamesCreator().questions_creator(state)
        # Call questions creator.
        if image is not None:
            msg = await bot.send_photo(chat_id=user_id, caption=question, photo=image, reply_markup=ikb)
        else:
            msg = await bot.send_message(chat_id=user_id, text=question, reply_markup=ikb)
        # Move on to the next question.
        data[GAME_QUESTION_NUMBER_REDIS_KEY] += 1
        # Remember question.
        data[GAME_QUESTION_REDIS_KEY] = question
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
