from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.backend.db import Base

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    genre = Column(String(100))
    country = Column(String(100))

    songs = relationship("Song", back_populates="artist")
