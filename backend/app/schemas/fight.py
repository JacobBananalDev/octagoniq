from pydantic import BaseModel
from typing import Optional


class FightCreate(BaseModel):
    """
    Schema for creating a Fight.
    """

    event_id: int
    fighter_1_id: int
    fighter_2_id: int
    winner_id: Optional[int] = None
    method: Optional[str] = None
    round: Optional[int] = None


class FightResponse(BaseModel):
    """
    Schema returned when sending Fight data back to client.
    """

    id: int
    event_id: int
    fighter_1_id: int
    fighter_2_id: int
    winner_id: Optional[int] = None
    method: Optional[str] = None
    round: Optional[int] = None

    class Config:
        from_attributes = True