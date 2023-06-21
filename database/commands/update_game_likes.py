from database import GamesInfo


async def update_game_likes(game_name: str) -> None:
    """
    :param game_name: Game name.
    :return: None.
    """

    await GamesInfo.update.values(likes=GamesInfo.likes+1).\
        where(GamesInfo.game_name == game_name).gino.status()
