from sqlalchemy import Column, Integer, String, DateTime
from API.DataBase.database import CurrentBaseAPI #Base, db_session
from sqlalchemy.sql import func


class IPAddress(CurrentBaseAPI.Base):
    __tablename__ = 'ipaddress'
    id = Column(Integer, primary_key=True, autoincrement="auto", unique=True, nullable=False)
    address = Column(String(20), unique=False, nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return f'<IPAddress: {self.address!r}, >'

    def save(self):
        CurrentBaseAPI.db_session.add(self)
        CurrentBaseAPI.db_session.commit()

    def delete(self):
        CurrentBaseAPI.db_session.remove(self)
        CurrentBaseAPI.db_session.commit()

    @staticmethod
    def find(id):
        return IPAddress.query.filter(IPAddress.id == id).first()

    @staticmethod
    def lastipaddress():
        row = CurrentBaseAPI.db_session.query(func.max(IPAddress.created_date)).first()
        if row is not None:
            maxdate = row[0] if row[0] is not None else None
        else:
            maxdate = None
        if not maxdate is None:
            return IPAddress.query.filter(IPAddress.created_date == maxdate).first()
        return None
