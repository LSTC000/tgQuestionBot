from database import GamesInfo


async def update_game_dislikes(game_name: str) -> None:
    """
    :param game_name: Game name.
    :return: None.
    """

    await GamesInfo.update.values(dislikes=GamesInfo.dislikes+1).\
        where(GamesInfo.game_name == game_name).gino.status()
