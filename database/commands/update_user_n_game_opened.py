from database import UsersAndGames


async def update_user_n_game_opened(user_id: int, game_name: str) -> None:
    """
    :param user_id: Telegram user id.
    :param game_name: Game name.
    :return: None.
    """

    await UsersAndGames.update.values(opened=UsersAndGames.opened+1).\
        where((UsersAndGames.user_id == user_id) & (UsersAndGames.game_name == game_name)).gino.status()
