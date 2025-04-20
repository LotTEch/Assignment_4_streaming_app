from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.backend.db import Base

class AccountType(Base):
    __tablename__ = 'account_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    ads_enabled = Column(Boolean, default=True)
    plan_type = Column(String(50))

    users = relationship("User", back_populates="account_type")  # Relasjon til User