from sqlalchemy.orm import Session
from app.models.subscription import Subscription

def create_subscription(db: Session, data: dict) -> Subscription:
    subscription = Subscription(**data)
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return subscription

def get_all_subscriptions(db: Session):
    return db.query(Subscription).all()

def get_subscription_by_id(db: Session, subscription_id: int):
    return db.query(Subscription).filter(Subscription.id == subscription_id).first()

def update_subscription(db: Session, subscription_id: int, data: dict):
    sub = get_subscription_by_id(db, subscription_id)
    if sub:
        for key, value in data.items():
            setattr(sub, key, value)
        db.commit()
        db.refresh(sub)
    return sub

def delete_subscription(db: Session, subscription_id: int):
    sub = get_subscription_by_id(db, subscription_id)
    if sub:
        db.delete(sub)
        db.commit()
        return True
    return False
