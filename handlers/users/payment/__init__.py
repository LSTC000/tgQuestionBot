__all__ = ['register_users_payment']


from .payment_clb import payment_clb
from .payment_msg import payment_msg
from .process_pre_checkout_query import process_pre_checkout_query

from aiogram import Dispatcher


def register_users_payment(dp: Dispatcher):
    dp.register_message_handler(payment_msg)
    dp.register_callback_query_handler(payment_clb)
    dp.register_pre_checkout_query_handler(process_pre_checkout_query)
