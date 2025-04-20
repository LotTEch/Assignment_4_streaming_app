from sqlalchemy.orm import Session
from app.models.songs import Song

def create_song(db: Session, data: dict) -> Song:
    new_song = Song(**data)
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song

def get_all_songs(db: Session):
    return db.query(Song).all()

def get_song_by_id(db: Session, song_id: int):
    return db.query(Song).filter(Song.id == song_id).first()

def update_song(db: Session, song_id: int, data: dict):
    song = get_song_by_id(db, song_id)
    if song:
        for key, value in data.items():
            setattr(song, key, value)
        db.commit()
        db.refresh(song)
    return song

def delete_song(db: Session, song_id: int):
    song = get_song_by_id(db, song_id)
    if song:
        db.delete(song)
        db.commit()
        return True
    return False
