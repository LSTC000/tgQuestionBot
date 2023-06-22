from loader import logger

from asyncpg import UniqueViolationError

from database import Reviews


async def add_user_review(user_id: int, target: str, target_name: str, review: str) -> None:
    '''
    :param user_id: Telegram user id.
    :param target: Enum: 'game' or 'test'.
    :param target_name: Name of the target.
    :param review: User review for the target.
    :return: None.
    '''

    try:
        user_review = Reviews(
            user_id=user_id,
            target=target,
            target_name=target_name,
            review=review
        )
        await user_review.create()
    except UniqueViolationError:
        logger.info('Error to add user review! User review already exists in the database.')
