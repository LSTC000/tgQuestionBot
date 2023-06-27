from loader import users_n_games_cache

from database import update_user_n_game_like


async def update_user_n_game_like_cache(user_id: int, game_name: str, value: bool) -> None:
    '''
    :param user_id: Telegram user_id.
    :param game_name: Game name.
    :param value: True if like, else False.
    :return: None.
    '''

    if user_id in users_n_games_cache.keys():
        if game_name in users_n_games_cache[user_id].keys():
            users_n_games_cache[user_id][game_name][0] = value

    await update_user_n_game_like(user_id=user_id, game_name=game_name, value=value)
