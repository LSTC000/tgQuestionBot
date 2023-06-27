__all__ = ['register_users_games']


from .games_creator import games_creator
from .games_like import games_like
from .games_dislike import games_dislike


from aiogram import Dispatcher


def register_users_games(dp: Dispatcher):
    dp.register_callback_query_handler(games_creator)
    dp.register_callback_query_handler(games_like)
    dp.register_callback_query_handler(games_dislike)
