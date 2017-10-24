from flask_user import UserMixin

from data_labeling.api.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    id: int = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username: str = db.Column(db.String(50), nullable=False, unique=True)
    password: str = db.Column(db.String(255), nullable=False, server_default='')

    def __init__(self, username: str, password_hash: str):
        self.username = username
        self.password = password_hash

