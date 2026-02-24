from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Event(Base):
    """
    Event model represents an MMA event (e.g., UFC 300)
    
    One event can contain multiple fights
    
    SQL Equivalent:
    CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    location VARCHAR,
    event_date DATE NOT NULL
);
    """
    
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True) # Example: UFC 300
    location = Column(String, nullable=True) #Example: Las Vegas, NV
    event_date = Column(Date, nullable=False)