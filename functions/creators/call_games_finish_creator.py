from data.redis import LAST_IKB_REDIS_KEY

from creators import GamesCreator

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_games_finish_creator(user_id: int, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Get answer and finish inline keyboard.
        answer, ikb = await GamesCreator().finish_creator(state)
        # Call finish creator.
        msg = await bot.send_message(chat_id=user_id, text=answer, reply_markup=ikb)
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
