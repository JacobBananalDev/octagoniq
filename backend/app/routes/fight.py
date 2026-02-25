from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.fight import FightCreate, FightResponse
from app.core.dependencies import require_admin
from app.models.user import User
from app.services import fight_service

router = APIRouter()


@router.post("/fights", response_model=FightResponse, status_code=201)
def create_fight(
    fight: FightCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    """
    Create fight (admin only).
    """

    result = fight_service.create_fight(db, fight)

    # If service returned error dict, convert to HTTPException
    if isinstance(result, dict) and "error" in result:

        error_message = result["error"]

        if "not found" in error_message.lower():
            raise HTTPException(status_code=404, detail=error_message)

        raise HTTPException(status_code=400, detail=error_message)

    return result