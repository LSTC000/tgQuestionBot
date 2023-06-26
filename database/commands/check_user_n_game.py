from database import UsersAndGames


async def check_user_n_game(user_id: int, game_name: str) -> bool:
    """
    :param user_id: Telegram user id.
    :param game_name: Game name.
    :return: True if user and game is exists, else False.
    """

    return True if await UsersAndGames.query.where(
        (UsersAndGames.user_id == user_id) &
        (UsersAndGames.game_name == game_name)
    ).gino.all() else False
