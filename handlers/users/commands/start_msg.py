from loader import dp, bot

from data.redis import LAST_IKB_REDIS_KEY

from data.messages import START_MESSAGE

from database import add_user_info

from functions import ikb_clear, check_user_info_cache

from keyboards import start_ikb

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(commands=['start'], state='*')
async def start_msg(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    # Clear previous inline keyboard.
    await ikb_clear(user_id=user_id, state=state)
    # We check whether there is information about the user in the database, if not, then add it there.
    if not await check_user_info_cache(user_id):
        await add_user_info(user_id, message.from_user.first_name)

    async with state.proxy() as data:
        # Clear all redis data for user.
        data.clear()
        # Call start inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=START_MESSAGE.format(message.from_user.first_name),
            reply_markup=start_ikb()
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
