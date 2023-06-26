from loader import logger

from asyncpg import UniqueViolationError

from database import UsersAndTests


async def add_user_n_test(user_id: int, test_name: str) -> None:
    '''
    :param user_id: Telegram user id.
    :param test_name: Test name.
    :return: None.
    '''

    try:
        user_n_test = UsersAndTests(
            user_id=user_id,
            test_name=test_name,
            opened=0,
            completed=0,
            like=False,
            dislike=False
        )
        await user_n_test.create()
    except UniqueViolationError:
        logger.info('Error to add user and test! User anf test already exists in the database.')
