from database import TestsInfo


async def check_test_info(test_name: str) -> bool:
    """
    :param test_name: Test name.
    :return: True if the test exists, else False.
    """

    return True if await TestsInfo.query.where(TestsInfo.test_name == test_name).gino.all() else False
