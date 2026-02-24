from pydantic import BaseModel
from typing import Optional
from datetime import date


class FighterCreate(BaseModel):
    """
    Schema used when creating a new fighter.

    This defines:
    - What fields the client must send
    - What types are expected
    - Default values (if any)
    """

    first_name: str
    last_name: str
    nickname: Optional[str] = None
    date_of_birth: Optional[date] = None
    height_cm: Optional[int] = None
    reach_cm: Optional[int] = None
    stance: Optional[str] = None
    wins: int = 0
    losses: int = 0
    draws: int = 0


class FighterResponse(BaseModel):
    """
    Schema used when returning a fighter from the API.

    This controls:
    - What fields are exposed to clients
    - The structure of the JSON response
    """

    id: int
    first_name: str
    last_name: str
    nickname: Optional[str] = None
    date_of_birth: Optional[date] = None
    height_cm: Optional[int] = None
    reach_cm: Optional[int] = None
    stance: Optional[str] = None
    wins: int
    losses: int
    draws: int

    class Config:
        # Allows Pydantic to read data directly from SQLAlchemy ORM objects
        # Instead of requiring a dictionary, it can accept model instances
        from_attributes = True