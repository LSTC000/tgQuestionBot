__all__ = ['register_users_payment']


from .payment_clb import payment_clb

from aiogram import Dispatcher


def register_users_payment(dp: Dispatcher):
    dp.register_callback_query_handler(payment_clb)
