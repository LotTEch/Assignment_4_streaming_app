from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.backend.db import Base
from datetime import datetime

class ListeningHistory(Base):
    __tablename__ = 'listening_history'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    song_id = Column(Integer, ForeignKey('songs.id'))
    listened_at = Column(DateTime, default=datetime.utcnow)
    device_used = Column(String(100))

    user = relationship("User", back_populates="listening_history")  # Relasjon til User
    song = relationship("Song", back_populates="listening_histories")  # Relasjon til Song