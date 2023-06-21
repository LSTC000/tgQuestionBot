from database import TestsInfo


async def update_test_completed_attempts(test_name: str) -> None:
    """
    :param test_name: Test name.
    :return: None.
    """

    await TestsInfo.update.values(completed_attempts=TestsInfo.completed_attempts+1).\
        where(TestsInfo.test_name == test_name).gino.status()
