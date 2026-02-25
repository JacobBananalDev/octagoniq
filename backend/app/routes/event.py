from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.event import EventCreate, EventResponse
from app.core.dependencies import require_admin
from app.models.user import User
from app.services import event_service

# Router groups all event-related endpoints
router = APIRouter()


@router.post("/events", response_model=EventResponse, status_code=201)
def create_event(
    event: EventCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    """
    Create a new event (admin only).

    Route responsibility:
    - Validate input
    - Enforce authorization
    - Call service layer
    - Return result
    """

    return event_service.create_event(db, event)


@router.get("/events", response_model=List[EventResponse])
def get_events(db: Session = Depends(get_db)):
    """
    Retrieve all events (public endpoint).

    No authentication required.
    """

    return event_service.get_all_events(db)


@router.get("/events/{event_id}", response_model=EventResponse)
def get_event_by_id(event_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific event by ID.

    - Returns 200 if found.
    - Returns 404 if not found.
    """

    event = event_service.get_event_by_id(db, event_id)

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event


@router.delete("/events/{event_id}", status_code=204)
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    """
    Delete an event (admin only).

    - Returns 204 if deleted.
    - Returns 404 if not found.
    """

    event = event_service.delete_event(db, event_id)

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return