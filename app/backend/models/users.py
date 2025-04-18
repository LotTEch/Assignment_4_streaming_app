from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base  # Oppdatert importbane

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, nullable=False)
    user_type = Column(String)
    registration_date = Column(Date)

    free_user = relationship("FreeUser", back_populates="user", uselist=False)
    premium_user = relationship("PremiumUser", back_populates="user", uselist=False)

class FreeUser(Base):
    __tablename__ = 'free_users'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    ads_enabled = Column(Boolean)

    user = relationship("User", back_populates="free_user")

class PremiumUser(Base):
    __tablename__ = 'premium_users'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    subscription_start = Column(Date)
    subscription_end = Column(Date)
    plan_type = Column(String)

    user = relationship("User", back_populates="premium_user")