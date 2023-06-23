__all__ = ['register_users_pickers']


from .call_games_picker import call_games_picker
from .call_tests_picker import call_tests_picker
from .process_games_picker import process_games_picker
from .process_tests_picker import process_tests_picker

from aiogram import Dispatcher


def register_users_pickers(dp: Dispatcher):
    dp.register_callback_query_handler(call_games_picker)
    dp.register_callback_query_handler(call_tests_picker)
    dp.register_callback_query_handler(process_games_picker)
    dp.register_callback_query_handler(process_tests_picker)