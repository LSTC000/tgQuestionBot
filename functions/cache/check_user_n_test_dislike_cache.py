from loader import users_n_test_cache

from database import check_user_n_test_like, check_user_n_test_dislike


async def check_user_n_test_dislike_cache(user_id: int, test_name: str) -> bool:
    '''
    :param user_id: Telegram user_id.
    :param test_name: Test name.
    :return: True if the dislike is True, else False.
    '''

    if user_id in users_n_test_cache.keys():
        if test_name in users_n_test_cache[user_id].keys():
            return users_n_test_cache[user_id][test_name][1]
        else:
            user_n_test_like = await check_user_n_test_like(user_id=user_id, test_name=test_name)
            user_n_test_dislike = await check_user_n_test_dislike(user_id=user_id, test_name=test_name)
            users_n_test_cache[user_id][test_name] = [user_n_test_like, user_n_test_dislike]
            return user_n_test_dislike
    else:
        user_n_test_like = await check_user_n_test_like(user_id=user_id, test_name=test_name)
        user_n_test_dislike = await check_user_n_test_dislike(user_id=user_id, test_name=test_name)
        users_n_test_cache[user_id] = {test_name: [user_n_test_like, user_n_test_dislike]}
        return user_n_test_dislike
