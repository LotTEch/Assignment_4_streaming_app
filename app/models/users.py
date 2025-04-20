from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base  # Oppdatert importbane

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    registration_date = Column(Date, default=None)
    account_type_id = Column(Integer, ForeignKey("account_types.id"))

    account_type = relationship("AccountType", back_populates="users")
    subscriptions = relationship("Subscription", back_populates="user")  # Relasjon til Subscription
    listening_history = relationship("ListeningHistory", back_populates="user")  # Relasjon til ListeningHistory
    
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