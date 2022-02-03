from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from main import app
from flask import current_app

class Database():

    def __init__(self, BASE_URL):
        self.engine = create_engine(BASE_URL)
        self.db_session = scoped_session(sessionmaker(autocommit=False,
                                                      autoflush=False,
                                                      bind=self.engine))
        self.Base = declarative_base()
        self.Base.query = self.db_session.query_property()

    def init_db(self):
        import API.DataBase.Models
        self.Base.metadata.create_all(bind=self.engine)

    def drop_db(self):
        import API.DataBase.Models
        self.Base.metadata.drop_all(bind=self.engine)


CurrentBaseAPI = Database(current_app.config["DATABASE_URL"])
