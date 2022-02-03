from sqlalchemy import Column, Integer, String, DateTime
from API.DataBase.database import CurrentBaseAPI
from sqlalchemy.sql import func


class Proxy(CurrentBaseAPI.Base):
    __tablename__ = 'proxies'
    id = Column(Integer, primary_key=True, autoincrement="auto", unique=True, nullable=False)
    address = Column(String(20), unique=False, nullable=False)
    port = Column(String(10), unique=False, nullable=False)
    type = Column(String(10), unique=False, nullable=False)
    country = Column(String(100), unique=False, nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, address, port, type, country):
        self.address = address
        self.port = port
        self.type = type
        self.country = country

    def __repr__(self):
        return f'<Proxy: {self.address!r}:{self.port} >'

    def save(self):
        CurrentBaseAPI.db_session.add(self)
        CurrentBaseAPI.db_session.commit()

    def delete(self):
        CurrentBaseAPI.db_session.remove(self)
        CurrentBaseAPI.db_session.commit()

    @staticmethod
    def find(id):
        return Proxy.query.filter(Proxy.id == id).first()

    @staticmethod
    def randomproxy():
        row = CurrentBaseAPI.db_session.query(func.max(Proxy.created_date)).first()
        if row is not None:
            maxdate = row[0] if row[0] is not None else None
        else:
            maxdate = None
        if not maxdate is None:
            return Proxy.query.filter(Proxy.created_date == maxdate).first()
        return None

