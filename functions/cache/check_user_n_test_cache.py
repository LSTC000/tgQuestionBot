from loader import users_n_test_cache

from database import check_user_n_test, check_user_n_test_like


async def check_user_n_test_cache(user_id: int, test_name: str) -> bool:
    '''
    :param user_id: Telegram user_id.
    :param test_name: Test name.
    :return: True if the user and game is exists, else False.
    '''

    if user_id in users_n_test_cache.keys():
        if test_name in users_n_test_cache[user_id]:
            return True
        else:
            user_n_test = await check_user_n_test(user_id=user_id, test_name=test_name)
            if user_n_test:
                users_n_test_cache[user_id][test_name] = await check_user_n_test_like(
                    user_id=user_id,
                    test_name=test_name
                )
            return user_n_test
    else:
        user_n_test = await check_user_n_test(user_id=user_id, test_name=test_name)
        if user_n_test:
            users_n_test_cache[user_id] = {
                test_name: await check_user_n_test_like(user_id=user_id, test_name=test_name)
            }
        return user_n_test
