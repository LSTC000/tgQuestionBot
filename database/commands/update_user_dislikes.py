from database import UsersInfo


async def update_user_dislikes(user_id: int) -> None:
    """
    :param user_id: Telegram user id.
    :return: None.
    """

    await UsersInfo.update.values(dislikes=UsersInfo.dislikes+1).\
        where(UsersInfo.user_id == user_id).gino.status()
