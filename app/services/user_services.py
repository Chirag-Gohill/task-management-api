from sqlalchemy.orm import Session
from ..models import User
from ..auth import hash_password, verify_password

def create_user(db: Session, username: str, password: str):
    hashed_pwd = hash_password(password)
    user = User(username=username, hashed_password=hashed_pwd)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user