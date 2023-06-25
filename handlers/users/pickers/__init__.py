__all__ = ['register_users_pickers']


from .games_picker import games_picker
from .tests_picker import tests_picker
from .process_games_picker import process_games_picker
from .process_tests_picker import process_tests_picker

from aiogram import Dispatcher


def register_users_pickers(dp: Dispatcher):
    dp.register_callback_query_handler(games_picker)
    dp.register_callback_query_handler(tests_picker)
    dp.register_callback_query_handler(process_games_picker)
    dp.register_callback_query_handler(process_tests_picker)
