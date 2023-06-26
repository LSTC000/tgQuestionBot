from database import UsersAndTests


async def check_users_n_tests_like(user_id: int, test_name: str) -> bool:
    """
    :param user_id: Telegram user id.
    :param test_name: Test name.
    :return: True if like is 1, else False.
    """

    return True if await UsersAndTests.query.where(
        (UsersAndTests.user_id == user_id) &
        (UsersAndTests.test_name == test_name) &
        (UsersAndTests.like == 1)
    ).gino.all() else False
