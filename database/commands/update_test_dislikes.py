from database import TestsInfo


async def update_test_dislikes(test_name: str) -> None:
    """
    :param test_name: Test name.
    :return: None.
    """

    await TestsInfo.update.values(dislikes=TestsInfo.dislikes+1).\
        where(TestsInfo.test_name == test_name).gino.status()
