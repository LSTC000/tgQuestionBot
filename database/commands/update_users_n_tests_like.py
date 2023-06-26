from database import UsersAndTests


async def update_users_n_tests_like(user_id: int, test_name: str, value: int) -> None:
    """
    :param user_id: Telegram user id.
    :param test_name: Game name.
    :param value: 1 or 0.
    :return: None.
    """

    await UsersAndTests.update.values(like=value).\
        where((UsersAndTests.user_id == user_id) & (UsersAndTests.test_name == test_name)).gino.status()
