from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.fighter import FighterCreate, FighterResponse, FighterUpdate
from app.core.dependencies import require_admin
from app.models.user import User
from app.services import fighter_service

router = APIRouter()


@router.post("/fighters", response_model=FighterResponse, status_code=201)
def create_fighter(
    fighter: FighterCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    """
    Create a new fighter (admin only).
    """

    return fighter_service.create_fighter(db, fighter)


@router.get("/fighters", response_model=List[FighterResponse])
def get_fighters(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    """
    Retrieve paginated list of fighters.
    """

    fighters = fighter_service.get_all_fighters(db)
    return fighters[skip : skip + limit]


@router.get("/fighters/{fighter_id}", response_model=FighterResponse)
def get_fighter_by_id(
    fighter_id: int,
    db: Session = Depends(get_db),
):
    """
    Retrieve a single fighter by ID.
    """

    fighter = fighter_service.get_fighter_by_id(db, fighter_id)

    if not fighter:
        raise HTTPException(status_code=404, detail="Fighter not found")

    return fighter


@router.patch("/fighters/{fighter_id}", response_model=FighterResponse)
def update_fighter(
    fighter_id: int,
    fighter_update: FighterUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    """
    Update fighter (admin only).
    """

    fighter = fighter_service.update_fighter(db, fighter_id, fighter_update)

    if not fighter:
        raise HTTPException(status_code=404, detail="Fighter not found")

    return fighter


@router.delete("/fighters/{fighter_id}", status_code=204)
def delete_fighter(
    fighter_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    """
    Delete fighter (admin only).
    """

    fighter = fighter_service.delete_fighter(db, fighter_id)

    if not fighter:
        raise HTTPException(status_code=404, detail="Fighter not found")

    return