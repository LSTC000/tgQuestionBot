from loader import dp, bot

from data.messages import ERROR_ENTER_PAYMENT_AMOUNT_MESSAGE

from data.config import PAYMENT_TOKEN, PAYMENT_TITLE, PAYMENT_DESCRIPTION

from functions import call_main_menu_ikb, check_user_alert_cache

from states import MainMenuStatesGroup, PaymentStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(state=PaymentStatesGroup.enter_amount)
async def payment_msg(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    try:
        amount = int(message.text)
        # Call the payment menu.
        await bot.send_invoice(
            chat_id=user_id,
            title=PAYMENT_TITLE,
            description=PAYMENT_DESCRIPTION,
            provider_token=PAYMENT_TOKEN,
            currency='rub',
            is_flexible=False,
            prices=[types.LabeledPrice(label='payment', amount=amount*100)],
            start_parameter='time-machine-example',
            payload='some-invoice-payload-for-our-internal-use'
        )
    except ValueError:
        # Inform the user about an error when entering the amount.
        await bot.send_message(chat_id=user_id, text=ERROR_ENTER_PAYMENT_AMOUNT_MESSAGE)
    # Call main inline menu.
    await call_main_menu_ikb(user_id=user_id, alert=await check_user_alert_cache(user_id), state=state)
    # Set main_menu_ikb state.
    await MainMenuStatesGroup.main_menu_ikb.set()
