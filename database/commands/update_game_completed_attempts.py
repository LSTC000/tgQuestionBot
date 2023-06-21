from database import GamesInfo


async def update_game_completed_attempts(game_name: str) -> None:
    """
    :param game_name: Game name.
    :return: None.
    """

    await GamesInfo.update.values(completed_attempts=GamesInfo.completed_attempts+1).\
        where(GamesInfo.game_name == game_name).gino.status()
