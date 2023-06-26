from loader import logger

from asyncpg import UniqueViolationError

from database import UsersAndGames


async def add_user_n_game(user_id: int, game_name: str) -> None:
    '''
    :param user_id: Telegram user id.
    :param game_name: Game name.
    :return: None.
    '''

    try:
        user_n_game = UsersAndGames(
            user_id=user_id,
            game_name=game_name,
            opened=0,
            completed=0,
            like=False,
            dislikes=False
        )
        await user_n_game.create()
    except UniqueViolationError:
        logger.info('Error to add user and game! User anf game already exists in the database.')
