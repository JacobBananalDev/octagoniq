from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.fighter import Fighter
from app.schemas.fighter import FighterCreate, FighterResponse
from typing import List

# Create a router instance
# This allows us to group fighter-related endpoints
router = APIRouter()


# Dependency to provide a database session per request
def get_db():
    """
    Creates a new database session for each request.

    Yields:
        db (Session): Active SQLAlchemy session

    Ensures:
        The session is properly closed after the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/fighters", response_model=FighterResponse, status_code=201)
def create_fighter(fighter: FighterCreate, db: Session = Depends(get_db)):
    """
    Create a new fighter in the database.

    Steps:
    1. Receive validated data from FighterCreate schema.
    2. Convert schema into SQLAlchemy model.
    3. Add model instance to session.
    4. Commit transaction.
    5. Refresh instance to get generated ID.
    6. Return clean response schema.
    """

    # Convert Pydantic schema into SQLAlchemy model instance
    db_fighter = Fighter(**fighter.dict())

    # Add the new fighter to the session
    db.add(db_fighter)

    # Commit the transaction (persist to database)
    db.commit()

    # Refresh the instance to load generated fields (like id)
    db.refresh(db_fighter)

    # Return the ORM object (FastAPI converts using response_model)
    return db_fighter

@router.get("/fighters", response_model=List[FighterResponse])
def get_fighters(db: Session = Depends(get_db)):
    """
    Retrieve all fighters from the database.

    Returns:
        A list of FighterResponse objects.
    """
    
    # Query all fighter records
    fighters = db.query(Fighter).all()
    
    return fighters

@router.get("/fighters/{fighter_id}", response_model=FighterResponse)
def get_fighter_by_id(fighter_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single fighter by ID.

    - If fighter exists → return 200 with fighter data.
    - If fighter does not exist → return 404 Not Found.
    """

    # Query database for fighter with matching ID
    fighter = db.query(Fighter).filter(Fighter.id == fighter_id).first()

    # If no fighter found, raise proper HTTP error
    if fighter is None:
        raise HTTPException(
            status_code=404,
            detail="Fighter not found"
        )

    return fighter