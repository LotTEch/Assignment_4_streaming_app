from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base

class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(255))
    created_date = Column(Date)
    song_count = Column(Integer, default=0)

    user = relationship("User", back_populates="playlists")
    songs = relationship("PlaylistSong", back_populates="playlist")
