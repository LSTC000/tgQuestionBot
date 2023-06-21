from database import GamesInfo


async def check_game_info(game_name: str) -> bool:
    """
    :param game_name: Game name.
    :return: True if the game exists, else False.
    """

    return True if await GamesInfo.query.where(GamesInfo.game_name == game_name).gino.all() else False
