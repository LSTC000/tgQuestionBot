import datetime

from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, VARCHAR, Integer, DateTime, sql, func


class GamesInfo(BaseModel):
    __tablename__ = 'games_info'

    # Game id.
    game_id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'games_info_id_seq\')'))
    # Game name.
    game_name = Column(VARCHAR(64), nullable=False)
    # Number of attempts.
    attempts = Column(Integer, nullable=False)
    # Number of completed attempts.
    completed_attempts = Column(Integer, nullable=False)
    # Game likes.
    likes = Column(Integer, nullable=False)
    # Game dislikes.
    dislikes = Column(Integer, nullable=False)
    # Created game date.
    created_date = Column(DateTime(True), server_default=func.now())
    # Update game date.
    updated_date = Column(
        DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=func.now()
    )

    query: sql.select
