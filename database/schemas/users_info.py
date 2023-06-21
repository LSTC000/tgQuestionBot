import datetime

from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, VARCHAR, Integer, DateTime, sql, func


class UsersInfo(BaseModel):
    __tablename__ = 'users_info'

    # Auto increment id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'users_info_id_seq\')'))
    # Telegram user id.
    user_id = Column(BigInteger, nullable=False)
    # Telegram user name.
    user_name = Column(VARCHAR(128), nullable=True)
    # Number of games opened by the user.
    opened_games = Column(Integer, nullable=False)
    # Number of games completed by the user.
    completed_games = Column(Integer, nullable=False)
    # Likes that the user has put.
    likes = Column(Integer, nullable=False)
    # Dislikes that the user has put.
    dislikes = Column(Integer, nullable=False)
    # Created user date.
    created_date = Column(DateTime(True), server_default=func.now())
    # Update user date.
    updated_date = Column(
        DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=func.now()
    )

    query: sql.select
