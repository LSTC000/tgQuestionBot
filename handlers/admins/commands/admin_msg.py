from loader import dp, bot

from data.config import ADMINS

from data.messages import ADMIN_MENU_MESSAGE

from keyboards import admin_menu_ikb

from functions import clear_last_ikb

from states import AdminMenuStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(commands=['admin'], state='*')
async def admin_command(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)

    if user_id in ADMINS:
        await bot.send_message(chat_id=user_id, text=ADMIN_MENU_MESSAGE, reply_markup=admin_menu_ikb)
        # Set admin_menu state.
        await AdminMenuStatesGroup.admin_menu.set()
