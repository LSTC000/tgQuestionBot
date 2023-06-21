from database import TestsInfo


async def update_test_attempts(test_name: str) -> None:
    """
    :param test_name: Test name.
    :return: None.
    """

    await TestsInfo.update.values(attempts=TestsInfo.attempts+1).\
        where(TestsInfo.test_name == test_name).gino.status()
