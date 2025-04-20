from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base

class PlaylistSong(Base):
    __tablename__ = 'playlist_songs'

    playlist_id = Column(Integer, ForeignKey('playlists.id'), primary_key=True)
    song_id = Column(Integer, ForeignKey('songs.id'), primary_key=True)
    added_date = Column(Date)
    position_in_playlist = Column(Integer)

    playlist = relationship("Playlist", back_populates="songs")
    song = relationship("Song", back_populates="playlists")
