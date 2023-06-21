from database import UsersInfo


async def update_user_completed_games(user_id: int) -> None:
    """
    :param user_id: Telegram user id.
    :return: None.
    """

    await UsersInfo.update.values(completed_games=UsersInfo.completed_games+1).\
        where(UsersInfo.user_id == user_id).gino.status()
