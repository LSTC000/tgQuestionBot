from loader import dp

from data.callbacks import GAMES_PICKER_CALLBACK_DATA

from functions import clear_last_ikb, call_games_picker

from states import MainMenuStatesGroup, PickersStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == GAMES_PICKER_CALLBACK_DATA, state=MainMenuStatesGroup.main_menu_ikb)
async def call_games_picker(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Call games picker inline menu.
    await call_games_picker(user_id=user_id, state=state)
    # Set games_picker state.
    await PickersStatesGroup.games_picker.set()
