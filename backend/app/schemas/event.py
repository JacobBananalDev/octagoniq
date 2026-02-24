from pydantic import BaseModel
from datetime import date
from typing import Optional, List

from app.schemas.fight import FightNestedResponse


# -------------------------
# Create Schema
# -------------------------

class EventCreate(BaseModel):
    """
    Schema for creating an Event.
    """

    name: str
    location: Optional[str] = None
    event_date: date


# -------------------------
# Basic Event Response
# -------------------------

class EventResponse(BaseModel):
    """
    Flat Event response (no fights included).
    """

    id: int
    name: str
    location: Optional[str] = None
    event_date: date

    class Config:
        from_attributes = True


# -------------------------
# Nested Event Response
# -------------------------

class EventWithFightsResponse(BaseModel):
    """
    Event response including nested fights and fighters.
    """

    id: int
    name: str
    location: Optional[str] = None
    event_date: date

    fights: List[FightNestedResponse] = []

    class Config:
        from_attributes = True