"""
api.py  Samlefil for å hente og manipulere data fra databasen.
Denne filen fungerer som et mellomlag mellom frontend (Streamlit) og backend (SQLAlchemy).
Hver funksjon åpner en databaseøkt med SessionLocal og utfører nødvendige operasjoner.
"""

from sqlalchemy.orm import Session
from app.backend.db import SessionLocal
from app.models.users import User
from app.models.songs import Song
from app.models.playlists import Playlist
from app.models.playlist_songs import PlaylistSong
from app.models.subscription import Subscription
from app.models.listening_history import ListeningHistory
from app.backend.models.account_types import AccountType  # Viktig import
from app.backend.models.artists import Artist


def get_account_types():
    return session.query(AccountType).all()



# ========================
# USERS
# ========================

def get_users():
    with SessionLocal() as session:
        return session.query(User).all()

def get_user_by_id(user_id: int):
    with SessionLocal() as session:
        return session.query(User).filter(User.id == user_id).first()

def create_user(data: dict):
    with SessionLocal() as session:
        user = User(**data)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

def update_user(user_id: int, data: dict):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in data.items():
                setattr(user, key, value)
            session.commit()
            session.refresh(user)
        return user

def delete_user(user_id: int):
    with SessionLocal() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False


# ========================
# SONGS
# ========================

def get_songs():
    with SessionLocal() as session:
        return session.query(Song).all()

def get_song_by_id(song_id: int):
    with SessionLocal() as session:
        return session.query(Song).filter(Song.id == song_id).first()

def create_song(data: dict):
    with SessionLocal() as session:
        song = Song(**data)
        session.add(song)
        session.commit()
        session.refresh(song)
        return song

def update_song(song_id: int, data: dict):
    with SessionLocal() as session:
        song = session.query(Song).filter(Song.id == song_id).first()
        if song:
            for key, value in data.items():
                setattr(song, key, value)
            session.commit()
            session.refresh(song)
        return song

def delete_song(song_id: int):
    with SessionLocal() as session:
        song = session.query(Song).filter(Song.id == song_id).first()
        if song:
            session.delete(song)
            session.commit()
            return True
        return False


# ========================
# PLAYLISTS
# ========================

def get_playlists():
    with SessionLocal() as session:
        return session.query(Playlist).all()

def get_playlist_by_id(playlist_id: int):
    with SessionLocal() as session:
        return session.query(Playlist).filter(Playlist.id == playlist_id).first()

def create_playlist(data: dict):
    with SessionLocal() as session:
        playlist = Playlist(**data)
        session.add(playlist)
        session.commit()
        session.refresh(playlist)
        return playlist

def update_playlist(playlist_id: int, data: dict):
    with SessionLocal() as session:
        playlist = session.query(Playlist).filter(Playlist.id == playlist_id).first()
        if playlist:
            for key, value in data.items():
                setattr(playlist, key, value)
            session.commit()
            session.refresh(playlist)
        return playlist

def delete_playlist(playlist_id: int):
    with SessionLocal() as session:
        playlist = session.query(Playlist).filter(Playlist.id == playlist_id).first()
        if playlist:
            session.delete(playlist)
            session.commit()
            return True
        return False

# Legg til sang i spilleliste
def add_song_to_playlist(playlist_id: int, song_id: int, position: int):
    with SessionLocal() as session:
        entry = PlaylistSong(
            playlist_id=playlist_id,
            song_id=song_id,
            position_in_playlist=position
        )
        session.add(entry)
        session.commit()
        session.refresh(entry)
        return entry

# Fjern sang fra spilleliste
def remove_song_from_playlist(playlist_id: int, song_id: int):
    with SessionLocal() as session:
        entry = session.query(PlaylistSong).filter_by(
            playlist_id=playlist_id, song_id=song_id
        ).first()
        if entry:
            session.delete(entry)
            session.commit()
            return True
        return False


# ========================
# SUBSCRIPTIONS
# ========================

def get_subscriptions():
    with SessionLocal() as session:
        return session.query(Subscription).all()

def get_subscription_by_id(subscription_id: int):
    with SessionLocal() as session:
        return session.query(Subscription).filter(Subscription.id == subscription_id).first()

def create_subscription(data: dict):
    with SessionLocal() as session:
        sub = Subscription(**data)
        session.add(sub)
        session.commit()
        session.refresh(sub)
        return sub

def update_subscription(subscription_id: int, data: dict):
    with SessionLocal() as session:
        sub = session.query(Subscription).filter(Subscription.id == subscription_id).first()
        if sub:
            for key, value in data.items():
                setattr(sub, key, value)
            session.commit()
            session.refresh(sub)
        return sub

def delete_subscription(subscription_id: int):
    with SessionLocal() as session:
        sub = session.query(Subscription).filter(Subscription.id == subscription_id).first()
        if sub:
            session.delete(sub)
            session.commit()
            return True
        return False


# ========================
# LISTENING HISTORY
# ========================

def get_listening_history():
    with SessionLocal() as session:
        return session.query(ListeningHistory).all()

def get_history_by_user(user_id: int):
    with SessionLocal() as session:
        return session.query(ListeningHistory).filter(ListeningHistory.user_id == user_id).all()

def create_listening_entry(data: dict):
    with SessionLocal() as session:
        entry = ListeningHistory(**data)
        session.add(entry)
        session.commit()
        session.refresh(entry)
        return entry

def delete_history_entry(history_id: int):
    with SessionLocal() as session:
        entry = session.query(ListeningHistory).filter(ListeningHistory.id == history_id).first()
        if entry:
            session.delete(entry)
            session.commit()
            return True
        return False


# ========================
# ARTISTS
# ========================
def get_artists():
    with SessionLocal() as session:
        return session.query(Artist).all()

def create_artist(data: dict):
    with SessionLocal() as session:
        artist = Artist(**data)
        session.add(artist)
        session.commit()
        session.refresh(artist)
        return artist

def update_artist(artist_id: int, data: dict):
    with SessionLocal() as session:
        artist = session.query(Artist).filter(Artist.id == artist_id).first()
        if artist:
            for key, value in data.items():
                setattr(artist, key, value)
            session.commit()
            session.refresh(artist)
        return artist

def delete_artist(artist_id: int):
    with SessionLocal() as session:
        artist = session.query(Artist).filter(Artist.id == artist_id).first()
        if artist:
            session.delete(artist)
            session.commit()
            return True
        return False

# ========================
# PLAYLISTS
# ========================
def get_playlists():
    with SessionLocal() as session:
        return session.query(Playlist).all()

def create_playlist(data: dict):
    with SessionLocal() as session:
        playlist = Playlist(**data)
        session.add(playlist)
        session.commit()
        session.refresh(playlist)
        return playlist

def update_playlist(playlist_id: int, data: dict):
    with SessionLocal() as session:
        playlist = session.query(Playlist).filter(Playlist.id == playlist_id).first()
        if playlist:
            for key, value in data.items():
                setattr(playlist, key, value)
            session.commit()
            session.refresh(playlist)
        return playlist

def delete_playlist(playlist_id: int):
    with SessionLocal() as session:
        playlist = session.query(Playlist).filter(Playlist.id == playlist_id).first()
        if playlist:
            session.delete(playlist)
            session.commit()
            return True
        return False