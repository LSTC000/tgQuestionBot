from database import UsersAndTests


async def update_user_n_test_dislike(user_id: int, game_name: str, value: bool) -> None:
    """
    :param user_id: Telegram user id.
    :param game_name: Game name.
    :param value: True or False.
    :return: None.
    """

    await UsersAndTests.update.values(dislike=value).\
        where((UsersAndTests.user_id == user_id) & (UsersAndTests.game_name == game_name)).gino.status()
