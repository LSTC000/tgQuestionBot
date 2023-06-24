__all__ = ['register_users_games']


from .naruto import naruto_questions

from aiogram import Dispatcher


def register_users_games(dp: Dispatcher):
    dp.register_callback_query_handler(naruto_questions)
