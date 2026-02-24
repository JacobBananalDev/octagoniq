from pydantic import BaseModel
from typing import Optional

# -------------------------
# Base / Create Schema
# -------------------------

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
    
    
# -------------------------
# Nested Fighter Schema
# -------------------------

class FighterNested(BaseModel):
    """
    Smaller Fighter schema used for nested responses.
    Prevents circular references.
    """

    id: int
    first_name: str
    last_name: str

    class Config:
        from_attributes = True


# -------------------------
# Basic Fight Response
# -------------------------

class FightResponse(BaseModel):
    """
    Flat fight response (IDs only).
    Used for standard fight CRUD endpoints.
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


# -------------------------
# Nested Fight Response
# -------------------------

class FightNestedResponse(BaseModel):
    """
    Fight response including nested fighter objects.
    Used inside EventWithFightsResponse.
    """

    id: int
    method: Optional[str] = None
    round: Optional[int] = None

    fighter_1: FighterNested
    fighter_2: FighterNested
    winner: Optional[FighterNested] = None

    class Config:
        from_attributes = True