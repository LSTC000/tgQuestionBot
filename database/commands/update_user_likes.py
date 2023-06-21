from database import UsersInfo


async def update_user_likes(user_id: int) -> None:
    """
    :param user_id: Telegram user id.
    :return: None.
    """

    await UsersInfo.update.values(likes=UsersInfo.likes+1).\
        where(UsersInfo.user_id == user_id).gino.status()
