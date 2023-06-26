from database import UsersAndGames


async def check_users_n_games_like(user_id: int, game_name: str) -> bool:
    """
    :param user_id: Telegram user id.
    :param game_name: Game name.
    :return: True if like is 1, else False.
    """

    return True if await UsersAndGames.query.where(
        (UsersAndGames.user_id == user_id) &
        (UsersAndGames.game_name == game_name) &
        (UsersAndGames.like == 1)
    ).gino.all() else False
