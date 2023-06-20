from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, SmallInteger, sql


class Alerts(BaseModel):
    __tablename__ = 'alerts'

    # Auto increment id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'alerts_id_seq\')'))
    # Telegram user id.
    user_id = Column(BigInteger, nullable=False)
    # 1 - alert, 0 - block alert.
    alert = Column(SmallInteger, nullable=False)

    query: sql.select
