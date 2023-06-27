from loader import users_n_test_cache

from database import update_user_n_test_dislike


async def update_user_n_test_dislike_cache(user_id: int, test_name: str, value: bool) -> None:
    '''
    :param user_id: Telegram user_id.
    :param test_name: Test name.
    :param value: True if dislike, else False.
    :return: None.
    '''

    if user_id in users_n_test_cache.keys():
        if test_name in users_n_test_cache[user_id].keys():
            users_n_test_cache[user_id][test_name][1] = value

    await update_user_n_test_dislike(user_id=user_id, test_name=test_name, value=value)
