from data.redis import LAST_IKB_REDIS_KEY

from data.messages import WAIT_CHAT_GPT_RESPONSE_MESSAGE

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
        # Wait Chat GPT response message.
        msg = await bot.send_message(chat_id=user_id, text=WAIT_CHAT_GPT_RESPONSE_MESSAGE)
        # Get Chat GPT answer and finish inline keyboard.
        answer, ikb = await GamesCreator().finish_creator(state)
        # Delete wait Chat GPT response message.
        await bot.delete_message(chat_id=user_id, message_id=msg.message_id)
        # Call finish creator.
        msg = await bot.send_message(chat_id=user_id, text=answer, reply_markup=ikb)
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
