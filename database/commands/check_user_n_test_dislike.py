from database import UsersAndTests


async def check_user_n_test_dislike(user_id: int, test_name: str) -> bool:
    """
    :param user_id: Telegram user id.
    :param test_name: Test name.
    :return: True if dislike is True, else False.
    """

    return True if await UsersAndTests.query.where(
        (UsersAndTests.user_id == user_id) &
        (UsersAndTests.test_name == test_name) &
        (UsersAndTests.dislike == True)
    ).gino.all() else False
