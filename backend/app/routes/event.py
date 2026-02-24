from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app.models.event import Event
from app.schemas.event import EventCreate, EventResponse

# Create router instance for grouping Event endpoints
router = APIRouter()


def get_db():
    """
    Dependency that provides a database session per request.

    Ensures:
    - A fresh session is created
    - The session is properly closed after the request
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/events", response_model=EventResponse, status_code=201)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
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


@router.get("/events/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single Event by ID.

    Returns:
    - 200 with Event data if found
    - 404 if not found
    """

    event = db.query(Event).filter(Event.id == event_id).first()

    if event is None:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event


@router.delete("/events/{event_id}", status_code=204)
def delete_event(event_id: int, db: Session = Depends(get_db)):
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