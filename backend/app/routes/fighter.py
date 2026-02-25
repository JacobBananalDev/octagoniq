from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.fighter import Fighter
from app.schemas.fighter import FighterCreate, FighterResponse, FighterUpdate
from typing import List
from app.core.dependencies import require_admin
from app.models.user import User

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
def create_fighter(
    fighter: FighterCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)):
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
def get_fighters(
    skip: int = Query(0, ge=10),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """
    Retrieve all fighters from the database.
    
   Query Parameters:
    - skip: must be >= 0
    - limit: must be between 1 and 100
    
    ge = greater than or equal to
    le = less than or equal to

    FastAPI will automatically return 422
    if values fall outside allowed range.

    Returns:
        A list of FighterResponse objects.
    """
    
    # Query all fighter records
    # offset = sql equivalent to OFFSET ?
    # limit = sql equivalent to LIMIT ?
    fighters = db.query(Fighter).offset(skip).limit(limit).all()
    
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

@router.delete("/fighters/{fighter_id}", status_code=204)
def delete_fighter(
    fighter_id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """
    Delete a fighter by ID.

    Returns:
    - 204 No Content if deleted successfully
    - 404 Not Found if fighter does not exist
    """

    fighter = db.query(Fighter).filter(Fighter.id == fighter_id).first()

    if fighter is None:
        raise HTTPException(
            status_code=404,
            detail="Fighter not found"
        )

    db.delete(fighter)
    db.commit()

    return

@router.patch("/fighters/{fighter_id}", response_model=FighterResponse)
def update_fighter(
    fighter_id: int,
    fighter_update: FighterUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    """
    Partially update a fighter.

    Only fields provided in request body will be updated.
    """

    fighter = db.query(Fighter).filter(Fighter.id == fighter_id).first()

    if fighter is None:
        raise HTTPException(
            status_code=404,
            detail="Fighter not found"
        )

    # Extract only provided fields (exclude unset ones)
    # use model_dump for Pydantic v2
    update_data = fighter_update.model_dump(exclude_unset=True)

    # Loop through fields and update dynamically
    for key, value in update_data.items():
        setattr(fighter, key, value)

    db.commit()
    db.refresh(fighter)

    return fighter