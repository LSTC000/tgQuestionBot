from loader import dp, bot

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from database import update_test_attempts

from functions import clear_last_ikb, clear_redis_data, call_main_menu_ikb, check_user_alert_cache

from pickers import TestsPicker

from states import MainMenuStatesGroup, PickersStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA, state=PickersStatesGroup.tests_picker)
async def process_tests_picker(callback: types.CallbackQuery, state: FSMContext) -> None:
    # Call process selection.
    pick, game_name = await TestsPicker().process_selection(
        callback=callback,
        callback_data=callback.data,
        state=state
    )
    # Check whether the user has made his choice.
    if pick:
        user_id = callback.from_user.id
        await bot.send_message(chat_id=user_id, text=f'Your choice: {game_name}')
        # Add 1 value for the test attempts.
        await update_test_attempts(game_name)
        # Clear last inline keyboard.
        await clear_last_ikb(user_id=user_id, state=state)
        # Clear redis data.
        await clear_redis_data(state)
        # Call main inline menu.
        await call_main_menu_ikb(user_id=user_id, alert=await check_user_alert_cache(user_id), state=state)
        # Set main_menu_ikb state.
        await MainMenuStatesGroup.main_menu_ikb.set()
