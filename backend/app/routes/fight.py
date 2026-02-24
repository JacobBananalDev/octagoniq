from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models.fight import Fight
from app.models.fighter import Fighter
from app.models.event import Event
from app.schemas.fight import FightCreate, FightResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/fights", response_model=FightResponse, status_code=201)
def create_fight(fight: FightCreate, db: Session = Depends(get_db)):
    """
    Create a Fight with validation:
    - Event must exist
    - Fighters must exist
    - Fighters cannot be the same person
    """

    # Validate event exists
    event = db.query(Event).filter(Event.id == fight.event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    # Validate fighter 1 exists
    fighter_1 = db.query(Fighter).filter(Fighter.id == fight.fighter_1_id).first()
    if fighter_1 is None:
        raise HTTPException(status_code=404, detail="Fighter 1 not found")

    # Validate fighter 2 exists
    fighter_2 = db.query(Fighter).filter(Fighter.id == fight.fighter_2_id).first()
    if fighter_2 is None:
        raise HTTPException(status_code=404, detail="Fighter 2 not found")

    # Prevent same fighter fighting themselves
    if fight.fighter_1_id == fight.fighter_2_id:
        raise HTTPException(
            status_code=400,
            detail="A fighter cannot fight themselves"
        )

    # Optional: validate winner exists if provided
    if fight.winner_id is not None:
        winner = db.query(Fighter).filter(Fighter.id == fight.winner_id).first()
        if winner is None:
            raise HTTPException(status_code=404, detail="Winner not found")

    db_fight = Fight(**fight.model_dump())
    db.add(db_fight)
    db.commit()
    db.refresh(db_fight)

    return db_fight