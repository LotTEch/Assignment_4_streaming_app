from sqlalchemy.orm import Session
from app.backend.db import SessionLocal
from app.backend.models.users import User
from app.backend.models.songs import Song

def get_users():
    """
    Henter alle brukere fra databasen.
    """
    with SessionLocal() as session:  # Opprett en database-økt
        users = session.query(User).all()  # Hent alle brukere
        return users

def get_songs():
    """
    Henter alle sanger fra databasen.
    """
    with SessionLocal() as session:  # Opprett en database-økt
        songs = session.query(Song).all()  # Hent alle sanger
        return songs