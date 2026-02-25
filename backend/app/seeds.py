from sqlalchemy.orm import Session

import app.models # ensures all models are registered

from app.database import SessionLocal
from app.models.fighter import Fighter


def seed_fighters(db: Session):
    fighters = [
        Fighter(
            first_name="Conor",
            last_name="McGregor",
            nickname="The Notorious",
            height_cm=175,
            reach_cm=188,
            stance="Southpaw",
            wins=22,
            losses=6,
            draws=0,
        ),
        Fighter(
            first_name="Khabib",
            last_name="Nurmagomedov",
            nickname="The Eagle",
            height_cm=178,
            reach_cm=178,
            stance="Orthodox",
            wins=29,
            losses=0,
            draws=0,
        ),
    ]

    for fighter in fighters:
        db.add(fighter)

    db.commit()


def main():
    db = SessionLocal()
    try:
        seed_fighters(db)
        print("Seed data inserted successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    main()