from sqlalchemy.orm import Session
from app.models.listening_history import ListeningHistory

def create_history(db: Session, data: dict) -> ListeningHistory:
    history = ListeningHistory(**data)
    db.add(history)
    db.commit()
    db.refresh(history)
    return history

def get_all_history(db: Session):
    return db.query(ListeningHistory).all()

def get_user_history(db: Session, user_id: int):
    return db.query(ListeningHistory).filter_by(user_id=user_id).all()

def delete_history_by_id(db: Session, history_id: int):
    h = db.query(ListeningHistory).filter_by(id=history_id).first()
    if h:
        db.delete(h)
        db.commit()
        return True
    return False
