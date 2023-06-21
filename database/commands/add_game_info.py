from loader import logger

from asyncpg import UniqueViolationError

from database import GamesInfo


async def add_game_info(game_name: str) -> None:
    '''
    :param game_name: Game name.
    :return: None.
    '''

    try:
        game_info = GamesInfo(
            game_name=game_name,
            attempts=0,
            completed_attempts=0,
            likes=0,
            dislikes=0
        )
        await game_info.create()
    except UniqueViolationError:
        logger.info('Error to add game info! Game info already exists in the database.')
