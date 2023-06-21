from database import UsersInfo


async def update_user_opened_games(user_id: int) -> None:
    """
    :param user_id: Telegram user id.
    :return: None.
    """

    await UsersInfo.update.values(opened_games=UsersInfo.opened_games+1).\
        where(UsersInfo.user_id == user_id).gino.status()
