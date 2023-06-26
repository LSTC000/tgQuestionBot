from loader import users_n_games_cache

from database import check_user_n_game, check_user_n_game_like


async def check_user_n_game_cache(user_id: int, game_name: str) -> bool:
    '''
    :param user_id: Telegram user_id.
    :param game_name: Game name.
    :return: True if the user and game is exists, else False.
    '''

    if user_id in users_n_games_cache.keys():
        if game_name in users_n_games_cache[user_id].keys():
            return True
        else:
            user_n_game = await check_user_n_game(user_id=user_id, game_name=game_name)
            if user_n_game:
                users_n_games_cache[user_id][game_name] = await check_user_n_game_like(
                    user_id=user_id,
                    game_name=game_name
                )
            return user_n_game
    else:
        user_n_game = await check_user_n_game(user_id=user_id, game_name=game_name)
        if user_n_game:
            users_n_games_cache[user_id] = {
                game_name: await check_user_n_game_like(user_id=user_id, game_name=game_name)
            }
        return user_n_game
