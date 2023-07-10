from data.redis import LAST_IKB_REDIS_KEY

from creators import TestsCreator

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_tests_finish_creator(user_id: int, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Get answer and finish inline keyboard.
        image, answer, ikb = await TestsCreator().finish_creator(state)
        # Call finish creator.
        if image is not None:
            msg = await bot.send_photo(chat_id=user_id, caption=answer, photo=image, reply_markup=ikb)
        else:
            msg = await bot.send_message(chat_id=user_id, text=answer, reply_markup=ikb)
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
