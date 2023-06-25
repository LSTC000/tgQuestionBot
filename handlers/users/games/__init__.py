__all__ = ['register_users_games']


from .questions_creator import questions_creator

from aiogram import Dispatcher


def register_users_games(dp: Dispatcher):
    dp.register_callback_query_handler(questions_creator)
