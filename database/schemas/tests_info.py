import datetime

from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, VARCHAR, Integer, DateTime, sql, func


class TestsInfo(BaseModel):
    __tablename__ = 'tests_info'

    # Auto increment id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'tests_info_id_seq\')'))
    # Test id.
    test_id = Column(Integer, nullable=False)
    # Test name.
    test_name = Column(VARCHAR(64), nullable=True)
    # Number of attempts.
    attempts = Column(Integer, nullable=False)
    # Number of completed attempts.
    completed_attempts = Column(Integer, nullable=False)
    # Game likes.
    likes = Column(Integer, nullable=False)
    # Game dislikes.
    dislikes = Column(Integer, nullable=False)
    # Created test date.
    created_date = Column(DateTime(True), server_default=func.now())
    # Update test date.
    updated_date = Column(
        DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=func.now()
    )

    query: sql.select
