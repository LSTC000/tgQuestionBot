from loader import dp

from data.callbacks import TESTS_PICKER_CALLBACK_DATA

from functions import clear_last_ikb, call_tests_picker

from states import MainMenuStatesGroup, PickersStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == TESTS_PICKER_CALLBACK_DATA, state=MainMenuStatesGroup.main_menu_ikb)
async def call_tests_picker(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Call tests picker inline menu.
    await call_tests_picker(user_id=user_id, state=state)
    # Set tests_picker state.
    await PickersStatesGroup.tests_picker.set()
