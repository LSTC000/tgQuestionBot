from loader import users_n_test_cache

from database import update_users_n_tests_like


async def update_user_n_test_like_cache(user_id: int, test_name: str, value: bool) -> None:
    '''
    :param user_id: Telegram user_id.
    :param test_name: Test name.
    :param value: True if like, else False.
    :return: None.
    '''

    if user_id in users_n_test_cache.keys():
        if test_name in users_n_test_cache[user_id].keys():
            users_n_test_cache[user_id][test_name] = value

    await update_users_n_tests_like(user_id=user_id, test_name=test_name, value=value)
