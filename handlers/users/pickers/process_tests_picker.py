from loader import dp, bot

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from database import update_test_attempts, update_user_opened_tests, update_user_n_test_opened, add_user_n_test

from functions import (
    clear_last_ikb,
    clear_redis_data,
    call_main_menu_ikb,
    check_user_alert_cache,
    check_user_n_test_cache
)

from pickers import TestsPicker

from states import MainMenuStatesGroup, PickersStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA, state=PickersStatesGroup.tests_picker)
async def process_tests_picker(callback: types.CallbackQuery, state: FSMContext) -> None:
    # Call process selection.
    pick, test_name = await TestsPicker().process_selection(
        callback=callback,
        callback_data=callback.data,
        state=state
    )
    # Check whether the user has made his choice.
    if pick:
        user_id = callback.from_user.id
        await bot.send_message(chat_id=user_id, text=f'Your choice: {test_name}')
        # Add 1 value for the test attempts.
        await update_test_attempts(test_name)
        # Add 1 value for the user opened tests.
        await update_user_opened_tests(user_id)
        # Check user and game in database and cache.
        if not await check_user_n_test_cache(user_id=user_id, test_name=test_name):
            await add_user_n_test(user_id=user_id, test_name=test_name)
        # Add 1 value for the user and game opened.
        await update_user_n_test_opened(user_id=user_id, test_name=test_name)
        # Clear last inline keyboard.
        await clear_last_ikb(user_id=user_id, state=state)
        # Clear redis data.
        await clear_redis_data(state)
        # Call main inline menu.
        await call_main_menu_ikb(user_id=user_id, alert=await check_user_alert_cache(user_id), state=state)
        # Set main_menu_ikb state.
        await MainMenuStatesGroup.main_menu_ikb.set()
