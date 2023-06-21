from loader import logger

from asyncpg import UniqueViolationError

from database import TestsInfo


async def add_test_info(test_name: str) -> None:
    '''
    :param test_name: Test name.
    :return: None.
    '''

    try:
        test_info = TestsInfo(
            test_name=test_name,
            attempts=0,
            completed_attempts=0,
            likes=0,
            dislikes=0
        )
        await test_info.create()
    except UniqueViolationError:
        logger.info('Error to add test info! Test info already exists in the database.')
