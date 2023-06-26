from database import UsersAndTests


async def update_users_n_tests_dislike(user_id: int, game_name: str, value: int) -> None:
    """
    :param user_id: Telegram user id.
    :param game_name: Game name.
    :param value: 1 or 0.
    :return: None.
    """

    await UsersAndTests.update.values(dislike=value).\
        where((UsersAndTests.user_id == user_id) & (UsersAndTests.game_name == game_name)).gino.status()
