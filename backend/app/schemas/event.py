from pydantic import BaseModel
from datetime import date
from typing import Optional


class EventCreate(BaseModel):
    """
    Schema used when creating a new Event.

    Defines:
    - What fields the client must provide
    - Expected types
    - Validation rules
    """

    name: str
    location: Optional[str] = None
    event_date: date


class EventResponse(BaseModel):
    """
    Schema returned to the client when sending Event data.

    Controls:
    - What fields are exposed
    - JSON structure of response
    """

    id: int
    name: str
    location: Optional[str] = None
    event_date: date

    class Config:
        # Allows Pydantic to serialize SQLAlchemy ORM objects directly
        from_attributes = True