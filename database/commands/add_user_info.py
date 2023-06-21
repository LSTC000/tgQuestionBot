from loader import logger

from asyncpg import UniqueViolationError

from database import UsersInfo


async def add_user_info(user_id: int, user_name: str) -> None:
    '''
    :param user_id: Telegram user id.
    :param user_name: Telegram user name.
    :return: None.
    '''

    try:
        user_info = UsersInfo(
            user_id=user_id,
            user_name=user_name,
            opened_games=0,
            completed_games=0,
            opened_tests=0,
            completed_tests=0,
            likes=0,
            dislikes=0
        )
        await user_info.create()
    except UniqueViolationError:
        logger.info('Error to add user info! User info already exists in the database.')
