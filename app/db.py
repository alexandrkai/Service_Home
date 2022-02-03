from flask_sqlalchemy import SQLAlchemy

conn = SQLAlchemy()
from sqlalchemy import create_engine
from flask import current_app
import app

engine = create_engine(app.app_context().config["SQLALCHEMY_DATABASE_URI"])
