from sqlalchemy import Integer, String
from . import db


class User(db.Model):
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(200), unique=True, nullable=False)
    password = db.Column(String(200), nullable=False)
    email = db.Column(String(200), unique=True, nullable=False)
