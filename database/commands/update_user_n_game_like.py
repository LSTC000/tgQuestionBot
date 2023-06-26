from database import UsersAndGames


async def update_user_n_game_like(user_id: int, game_name: str, value: int) -> None:
    """
    :param user_id: Telegram user id.
    :param game_name: Game name.
    :param value: 1 or 0.
    :return: None.
    """

    await UsersAndGames.update.values(like=value).\
        where((UsersAndGames.user_id == user_id) & (UsersAndGames.game_name == game_name)).gino.status()
