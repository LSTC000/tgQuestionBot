from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, VARCHAR, TEXT, DateTime, sql, func


class Reviews(BaseModel):
    __tablename__ = 'reviews'

    # Autoincrement id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'reviews_id_seq\')'))
    # Telegram user id.
    user_id = Column(BigInteger, nullable=False)
    # Enum: 'game' or 'test'.
    target = Column(VARCHAR(16), nullable=False)
    # Name of the target.
    target_name = Column(VARCHAR(64), nullable=False)
    # Review of the game.
    review = Column(TEXT, nullable=True)
    # Created review date.
    created_date = Column(DateTime(True), server_default=func.now())

    query: sql.select
