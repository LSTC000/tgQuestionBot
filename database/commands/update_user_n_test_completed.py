from database import UsersAndTests


async def update_user_n_test_completed(user_id: int, test_name: str) -> None:
    """
    :param user_id: Telegram user id.
    :param test_name: Test name.
    :return: None.
    """

    await UsersAndTests.update.values(completed=UsersAndTests.completed+1).\
        where((UsersAndTests.user_id == user_id) & (UsersAndTests.test_name == test_name)).gino.status()
