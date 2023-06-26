import datetime

from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, SmallInteger, VARCHAR, Integer, DateTime, sql, func


class UsersAndTests(BaseModel):
    __tablename__ = 'users_n_tests'

    # Autoincrement id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'users_n_tests_id_seq\')'))
    # Telegram user id.
    user_id = Column(BigInteger, nullable=False)
    # Test name.
    test_name = Column(VARCHAR(64), nullable=False)
    # Number of tests opened by the user.
    opened = Column(Integer, nullable=False)
    # Number of tests completed by the user.
    completed = Column(Integer, nullable=False)
    # Like that the user gave to the test (1 or 0).
    like = Column(SmallInteger, nullable=False)
    # Dislike that the user gave to the test (1 or 0).
    dislike = Column(SmallInteger, nullable=False)
    # Created users and tests date.
    created_date = Column(DateTime(True), server_default=func.now())
    # Update users and tests date.
    updated_date = Column(
        DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=func.now()
    )

    query: sql.select
