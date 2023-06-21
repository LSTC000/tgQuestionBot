from loader import users_info_cache

from database import check_user_info


async def check_user_info_cache(user_id: int) -> bool:
    '''
    :param user_id: Telegram user_id.
    :return: True if user information exists, else False.
    '''

    if user_id in users_info_cache.keys():
        return True
    else:
        if await check_user_info(user_id):
            users_info_cache[user_id] = {}
            return True

    return False
