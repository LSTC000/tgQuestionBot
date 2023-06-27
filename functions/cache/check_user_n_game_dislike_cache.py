from loader import users_n_games_cache

from database import check_user_n_game_like, check_user_n_game_dislike


async def check_user_n_game_dislike_cache(user_id: int, game_name: str) -> bool:
    '''
    :param user_id: Telegram user_id.
    :param game_name: Game name.
    :return: True if the dislike is True, else False.
    '''

    if user_id in users_n_games_cache.keys():
        if game_name in users_n_games_cache[user_id].keys():
            return users_n_games_cache[user_id][game_name][1]
        else:
            user_n_game_like = await check_user_n_game_like(user_id=user_id, game_name=game_name)
            user_n_game_dislike = await check_user_n_game_dislike(user_id=user_id, game_name=game_name)
            users_n_games_cache[user_id][game_name] = [user_n_game_like, user_n_game_dislike]
            return user_n_game_dislike
    else:
        user_n_game_like = await check_user_n_game_like(user_id=user_id, game_name=game_name)
        user_n_game_dislike = await check_user_n_game_dislike(user_id=user_id, game_name=game_name)
        users_n_games_cache[user_id] = {game_name: [user_n_game_like, user_n_game_dislike]}
        return user_n_game_dislike
