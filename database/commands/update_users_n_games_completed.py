from database import UsersAndGames


async def update_users_n_games_completed(user_id: int, game_name: str) -> None:
    """
    :param user_id: Telegram user id.
    :param game_name: Game name.
    :return: None.
    """

    await UsersAndGames.update.values(completed=UsersAndGames.completed+1).\
        where((UsersAndGames.user_id == user_id) & (UsersAndGames.game_name == game_name)).gino.status()
