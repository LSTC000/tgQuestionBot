from database import UsersAndTests


async def check_user_n_test(user_id: int, test_name: str) -> bool:
    """
    :param user_id: Telegram user id.
    :param test_name: Test name.
    :return: True if user and test is exists, else False.
    """

    return True if await UsersAndTests.query.where(
        (UsersAndTests.user_id == user_id) &
        (UsersAndTests.test_name == test_name)
    ).gino.all() else False
