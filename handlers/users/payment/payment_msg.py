from loader import dp, bot

from data.messages import ERROR_ENTER_PAYMENT_AMOUNT_MESSAGE

from data.config import RECEIVER, QUICKPAY_FORM, TARGETS, PAYMENT_TYPE

from functions import call_payment_ikb, call_main_menu_ikb, check_user_alert_cache

from states import MainMenuStatesGroup, PaymentStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from yoomoney import Quickpay


@dp.message_handler(state=PaymentStatesGroup.enter_amount)
async def payment_msg(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id

    try:
        amount = int(message.text)

        if amount > 0:
            # Call the payment menu.
            quickpay = Quickpay(
                receiver=RECEIVER,
                quickpay_form=QUICKPAY_FORM,
                targets=TARGETS,
                paymentType=PAYMENT_TYPE,
                sum=amount
            )
            # Call payment inline menu.
            await call_payment_ikb(user_id=user_id, redirected_url=quickpay.redirected_url, amount=amount, state=state)
        else:
            # Inform the user about an error when entering the amount.
            await bot.send_message(chat_id=user_id, text=ERROR_ENTER_PAYMENT_AMOUNT_MESSAGE)
            # Call main inline menu.
            await call_main_menu_ikb(user_id=user_id, alert=await check_user_alert_cache(user_id), state=state)
            # Set main_menu_ikb state.
            await MainMenuStatesGroup.main_menu_ikb.set()
    except ValueError:
        # Inform the user about an error when entering the amount.
        await bot.send_message(chat_id=user_id, text=ERROR_ENTER_PAYMENT_AMOUNT_MESSAGE)
        # Call main inline menu.
        await call_main_menu_ikb(user_id=user_id, alert=await check_user_alert_cache(user_id), state=state)
        # Set main_menu_ikb state.
        await MainMenuStatesGroup.main_menu_ikb.set()
