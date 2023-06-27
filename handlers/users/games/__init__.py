__all__ = ['register_users_games']


from .games_creator import games_creator

from aiogram import Dispatcher


def register_users_games(dp: Dispatcher):
    dp.register_callback_query_handler(games_creator)
