from loader import dp, bot

from data.callbacks import PAYMENT_CALLBACK_DATA

from data.messages import ENTER_PAYMENT_AMOUNT_MESSAGE

from functions import clear_last_ikb

from states import MainMenuStatesGroup, PaymentStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == PAYMENT_CALLBACK_DATA, state=MainMenuStatesGroup.main_menu_ikb)
async def payment_clb(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Withdrawal of the request for the introduction of the amount.
    await bot.send_message(chat_id=user_id, text=ENTER_PAYMENT_AMOUNT_MESSAGE)
    # Set enter_amount state.
    await PaymentStatesGroup.enter_amount.set()
