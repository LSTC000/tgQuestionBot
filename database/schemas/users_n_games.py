import datetime

from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, BOOLEAN, VARCHAR, Integer, DateTime, sql, func


class UsersAndGames(BaseModel):
    __tablename__ = 'users_n_games'

    # Autoincrement id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'users_n_games_id_seq\')'))
    # Telegram user id.
    user_id = Column(BigInteger, nullable=False)
    # Game name.
    game_name = Column(VARCHAR(64), nullable=False)
    # Number of games opened by the user.
    opened = Column(Integer, nullable=False)
    # Number of games completed by the user.
    completed = Column(Integer, nullable=False)
    # Like that the user gave to the game (True or False).
    like = Column(BOOLEAN, nullable=False)
    # Dislike that the user gave to the game (True or False).
    dislike = Column(BOOLEAN, nullable=False)
    # Created users and games date.
    created_date = Column(DateTime(True), server_default=func.now())
    # Update users and games date.
    updated_date = Column(
        DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=func.now()
    )

    query: sql.select
