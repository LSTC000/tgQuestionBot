__all__ = ['register_users_commands']


from .start_msg import start_msg

from aiogram import Dispatcher


def register_users_commands(dp: Dispatcher):
    dp.register_message_handler(start_msg)
