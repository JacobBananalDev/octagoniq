from sqlalchemy.orm import Session
from app.models.fighter import Fighter
from app.schemas.fighter import FighterCreate, FighterUpdate


def create_fighter(db: Session, fighter_data: FighterCreate):
    """
    Business logic for creating a new fighter.
    
     Steps:
    1. Receive validated data from FighterCreate schema.
    2. Convert schema into SQLAlchemy model.
    3. Add model instance to session.
    4. Commit transaction.
    5. Refresh instance to get generated ID.
    6. Return clean response schema.
    """

    fighter = Fighter(**fighter_data.model_dump())
    db.add(fighter) # add the new fighter to the session
    db.commit() # commit the transaction (persist to database)
    db.refresh(fighter) # refresh the instance to load generated fields (like id)

    # return the ORM object (FastAPI convets using response_model)
    return fighter


def get_all_fighters(db: Session):
    """
    Retrieves all fighters from the database.

    This function contains no HTTP logic.
    It simply interacts with the data layer.
    """

    return db.query(Fighter).all()


def update_fighter(db: Session, fighter_id: int, fighter_data: FighterUpdate):
    """
    Updates an existing fighter.

    - Fetches fighter by ID
    - Applies only provided fields (partial update support)
    - Commits changes
    - Returns updated fighter
    """

    fighter = db.query(Fighter).filter(Fighter.id == fighter_id).first()

    if not fighter:
        return None

    # Only update fields that were provided in request body
    update_data = fighter_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(fighter, key, value)

    db.commit()
    db.refresh(fighter)

    return fighter


def delete_fighter(db: Session, fighter_id: int):
    """
    Deletes a fighter from the database.

    - Fetches fighter by ID
    - Removes record if found
    - Commits transaction
    """

    fighter = db.query(Fighter).filter(Fighter.id == fighter_id).first()

    if not fighter:
        return None

    db.delete(fighter)
    db.commit()

    return fighter

def get_fighter_by_id(db: Session, fighter_id: int):
    return db.query(Fighter).filter(Fighter.id == fighter_id).first()