from data.redis import LAST_IKB_REDIS_KEY, PICKER_PAGE_REDIS_KEY

from data.messages import GAMES_PICKER_MESSAGE

from pickers import GamesPicker

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_games_picker(user_id: int, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Set start page for games picker.
        start_page = 0
        data[PICKER_PAGE_REDIS_KEY] = start_page
        # Call games picker inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=GAMES_PICKER_MESSAGE,
            reply_markup=await GamesPicker().games_picker(start_page)
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
