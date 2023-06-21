from database import UsersInfo


async def update_user_completed_tests(user_id: int) -> None:
    """
    :param user_id: Telegram user id.
    :return: None.
    """

    await UsersInfo.update.values(completed_tests=UsersInfo.completed_tests+1).\
        where(UsersInfo.user_id == user_id).gino.status()
