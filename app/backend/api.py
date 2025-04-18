from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.models.users import User

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()