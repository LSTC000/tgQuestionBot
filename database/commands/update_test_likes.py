from database import TestsInfo


async def update_test_likes(test_name: str) -> None:
    """
    :param test_name: Test name.
    :return: None.
    """

    await TestsInfo.update.values(likes=TestsInfo.likes+1).\
        where(TestsInfo.test_name == test_name).gino.status()
