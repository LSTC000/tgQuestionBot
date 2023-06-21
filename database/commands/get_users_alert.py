from database import Alerts

from sqlalchemy import select, func
from sqlalchemy.exc import ArgumentError


async def get_users_alert() -> list:
    """
    :return: A list with users who have enabled notifications.
    """

    try:
        return await select([func.distinct(Alerts.user_id)]).gino.all()
    except ArgumentError:
        return []
