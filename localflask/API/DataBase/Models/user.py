from sqlalchemy import Column, Integer, String
# from DataBase.database import Base, db_session
from API.DataBase.database import CurrentBaseAPI

class User(CurrentBaseAPI.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'

    def save(self):
        CurrentBaseAPI.db_session.add(self)
        CurrentBaseAPI.db_session.commit()
