from loader import dp

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from functions import last_ikb_clear, call_main_menu_ikb, check_user_alert_cache

from states import MainMenuStatesGroup, PickersStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(
    lambda c: c.data == CANCEL_TO_MAIN_MENU_CALLBACK_DATA,
    state=[PickersStatesGroup.games_picker]
)
async def cancel_to_main_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await last_ikb_clear(user_id=user_id, state=state)
    # Call main inline menu.
    await call_main_menu_ikb(user_id=user_id, alert=await check_user_alert_cache(user_id), state=state)
    # Set main_menu_ikb state.
    await MainMenuStatesGroup.main_menu_ikb.set()
