from sqlalchemy.orm import Session
from app.models.users import User

def create_user(db: Session, data: dict) -> User:
    new_user = User(**data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session) -> list[User]:
    return db.query(User).all()

def get_user_by_id(db: Session, id: int) -> User | None:
    return db.query(User).filter(User.id == id).first()

def update_user(db: Session, id: int, data: dict) -> User | None:
    user = db.query(User).filter(User.id == id).first()
    if user:
        for key, value in data.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, id: int) -> bool:
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
