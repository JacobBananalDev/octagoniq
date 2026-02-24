from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.fighter import Fighter
from app.schemas.fighter import FighterCreate, FighterResponse

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