from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List

from app.database import get_db
from app.models.event import Event
from app.models.fight import Fight
from app.schemas.event import EventCreate, EventResponse, EventWithFightsResponse
from app.core.dependencies import require_admin
from app.models.user import User

# Create router instance for grouping Event endpoints
router = APIRouter()


@router.post("/events", response_model=EventResponse, status_code=201)
def create_event(
    event: EventCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """
    Create a new Event.

    Steps:
    1. Receive validated EventCreate schema.
    2. Convert to SQLAlchemy model.
    3. Add to session.
    4. Commit transaction.
    5. Refresh to get generated ID.
    """

    # Convert validated schema into ORM model
    db_event = Event(**event.model_dump())

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event


@router.get("/events", response_model=List[EventResponse])
def get_events(db: Session = Depends(get_db)):
    """
    Retrieve all events from the database.
    """

    return db.query(Event).all()


@router.get("/events/{event_id}", response_model=EventWithFightsResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single Event by ID.

    Returns:
    - 200 with Event data if found
    - 404 if not found
    """

    event = (
    db.query(Event)
    .options(
        joinedload(Event.fights)
        .joinedload(Fight.fighter_1),
        joinedload(Event.fights)
        .joinedload(Fight.fighter_2),
        joinedload(Event.fights)
        .joinedload(Fight.winner),
    )
    .filter(Event.id == event_id)
    .first()
    )

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event


@router.delete("/events/{event_id}", status_code=204)
def delete_event(
    event_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """
    Delete an Event by ID.

    Returns:
    - 204 No Content if deleted
    - 404 if Event does not exist
    """

    event = db.query(Event).filter(Event.id == event_id).first()

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    db.delete(event)
    db.commit()