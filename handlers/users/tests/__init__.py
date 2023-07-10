__all__ = ['register_users_tests']


from .tests_creator import tests_creator
from .tests_like import tests_like
from .tests_dislike import tests_dislike
from .tests_review_clb import tests_review_clb
from .tests_review_msg import tests_review_msg


from aiogram import Dispatcher


def register_users_tests(dp: Dispatcher):
    dp.register_callback_query_handler(tests_creator)
    dp.register_callback_query_handler(tests_like)
    dp.register_callback_query_handler(tests_dislike)
    dp.register_callback_query_handler(tests_review_clb)
    dp.register_message_handler(tests_review_msg)
