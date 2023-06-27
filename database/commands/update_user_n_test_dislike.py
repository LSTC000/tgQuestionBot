from database import UsersAndTests


async def update_user_n_test_dislike(user_id: int, test_name: str, value: bool) -> None:
    """
    :param user_id: Telegram user id.
    :param test_name: Game name.
    :param value: True or False.
    :return: None.
    """

    await UsersAndTests.update.values(dislike=value).\
        where((UsersAndTests.user_id == user_id) & (UsersAndTests.test_name == test_name)).gino.status()
