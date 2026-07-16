from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class User(Base):
    __tablename__ = "users" # This is the actual name of the table in PostgreSQL

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, nullable=False)
    
    # We never store plain-text passwords, only the hashed versions
    hashed_password = Column(String, nullable=False)
    
    is_active = Column(Boolean, default=True)