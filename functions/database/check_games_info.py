from data.config import GAMES_NAME

from database import check_game_info, add_game_info


async def check_games_info() -> None:
    '''
    Checks if the game is in the database, if it is not there, then adds it there.
    :return: None.
    '''

    for game_name in GAMES_NAME:
        if not await check_game_info(game_name):
            await add_game_info(game_name)
