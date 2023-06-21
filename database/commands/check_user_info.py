from database import UsersInfo


async def check_user_info(user_id: int) -> bool:
    """
    :param user_id: Telegram user id.
    :return: True if user information exists, else False.
    """

    return True if await UsersInfo.query.where(UsersInfo.user_id == user_id).gino.all() else False
