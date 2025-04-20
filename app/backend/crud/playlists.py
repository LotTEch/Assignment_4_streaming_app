from sqlalchemy.orm import Session  # Import Session from SQLAlchemy
from app.models.playlist_songs import PlaylistSong

def add_song_to_playlist(db: Session, playlist_id: int, song_id: int, position: int) -> PlaylistSong:
    entry = PlaylistSong(
        playlist_id=playlist_id,
        song_id=song_id,
        position_in_playlist=position
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

def remove_song_from_playlist(db: Session, playlist_id: int, song_id: int) -> bool:
    entry = db.query(PlaylistSong).filter_by(playlist_id=playlist_id, song_id=song_id).first()
    if entry:
        db.delete(entry)
        db.commit()
        return True
    return False