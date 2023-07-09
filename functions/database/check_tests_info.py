from data.config import TESTS_NAMES

from database import check_test_info, add_test_info


async def check_tests_info() -> None:
    '''
    Checks if the test is in the database, if it is not there, then adds it there.
    :return: None.
    '''

    for test_name in TESTS_NAMES:
        if not await check_test_info(test_name):
            await add_test_info(test_name)
