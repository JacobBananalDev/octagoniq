from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.database import Base


class Fighter(Base):
    """
    Fighter model represents an MMA fighter.

    Each instance of this class corresponds
    to one row in the 'fighters' table.
    """

    # This tells SQLAlchemy what the table name should be
    __tablename__ = "fighters"

    # Primary Key (unique identifier for each fighter)
    id = Column(Integer, primary_key=True, index=True)

    # Basic fighter information
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    nickname = Column(String, nullable=True)

    # Date of birth
    date_of_birth = Column(Date, nullable=True)

    # Physical stats
    height_cm = Column(Integer, nullable=True)
    reach_cm = Column(Integer, nullable=True)
    stance = Column(String, nullable=True)

    # Record stats
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    draws = Column(Integer, default=0)
    
    fights_as_fighter_1 = relationship(
        "Fight",
        foreign_keys="Fight.fighter_1_id",
        back_populates="fighter_1"
    )

    fights_as_fighter_2 = relationship(
        "Fight",
        foreign_keys="Fight.fighter_2_id",
        back_populates="fighter_2"
    )