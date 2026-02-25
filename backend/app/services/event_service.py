from sqlalchemy.orm import Session
from app.models.event import Event
from app.schemas.event import EventCreate


def create_event(db: Session, event_data: EventCreate):
    """
    Business logic for creating a new event.

    Steps:
    1. Receive validated schema (EventCreate).
    2. Convert schema into SQLAlchemy ORM model.
    3. Add event to session.
    4. Commit transaction.
    5. Refresh instance to load generated fields (id).
    6. Return ORM object.
    """

    event = Event(**event_data.model_dump())

    db.add(event)              # Stage event for insertion
    db.commit()                # Persist to database
    db.refresh(event)          # Load generated fields (id, timestamps)

    return event


def get_all_events(db: Session):
    """
    Retrieve all events from the database.

    No HTTP logic here.
    Pure data-layer interaction.
    """

    return db.query(Event).all()


def get_event_by_id(db: Session, event_id: int):
    """
    Retrieve a single event by its ID.

    Returns:
        Event ORM object if found,
        None if not found.
    """

    return db.query(Event).filter(Event.id == event_id).first()


def delete_event(db: Session, event_id: int):
    """
    Delete an event by ID.

    Steps:
    1. Fetch event.
    2. If not found → return None.
    3. Delete from session.
    4. Commit transaction.
    """

    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        return None

    db.delete(event)  # Mark for deletion
    db.commit()       # Persist removal

    return event