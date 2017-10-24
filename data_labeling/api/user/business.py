from flask_user import UserManager

from data_labeling.api.database import db
from data_labeling.api.database.models import User

user_manager = UserManager()

def create_user(username: str, password: str) -> int:
    password_hash = user_manager.hash_password(password)
    new_user = User(username, password_hash)

    db.session.add(new_user)
    db.session.commit()
    return new_user.id