from database import UsersAndTests


async def update_user_n_test_opened(user_id: int, test_name: str) -> None:
    """
    :param user_id: Telegram user id.
    :param test_name: Test name.
    :return: None.
    """

    await UsersAndTests.update.values(opened=UsersAndTests.opened+1).\
        where((UsersAndTests.user_id == user_id) & (UsersAndTests.test_name == test_name)).gino.status()
