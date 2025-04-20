from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base

class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    genre = Column(String)
    release_date = Column(Date)
    artist_id = Column(Integer, ForeignKey('artists.id'))

    artist = relationship("Artist", back_populates="songs")
    listening_histories = relationship("ListeningHistory", back_populates="song")  # Relasjon til ListeningHistory