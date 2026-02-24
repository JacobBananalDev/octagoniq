from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Fight(Base):
    """
    Fight model represents a matchup between two fighters
    at a specific event.
    
    SQL:
    FOREIGN KEY (event_id) REFERENCES events(id)
    FOREIGN KEY (fighter_1_id) REFERENCES fighters(id)
    FOREIGN KEY (fighter_2_id) REFERENCES fighters(id)
    FOREIGN KEY (winner_id) REFERENCES fighters(id)
    """

    __tablename__ = "fights"

    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to Event
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)

    # Foreign keys to Fighter
    fighter_1_id = Column(Integer, ForeignKey("fighters.id"), nullable=False)
    fighter_2_id = Column(Integer, ForeignKey("fighters.id"), nullable=False)

    # Winner (can be null if fight hasn't happened yet)
    winner_id = Column(Integer, ForeignKey("fighters.id"), nullable=True)

    method = Column(String, nullable=True)   # KO, Submission, Decision
    round = Column(Integer, nullable=True)
    
    # ORM (Object-Relational Mapping) Relationships
    event = relationship("Event", back_populates="fights")

    fighter_1 = relationship(
        "Fighter",
        foreign_keys=[fighter_1_id],
        back_populates="fights_as_fighter_1"
    )

    fighter_2 = relationship(
        "Fighter",
        foreign_keys=[fighter_2_id],
        back_populates="fights_as_fighter_2"
    )

    winner = relationship(
        "Fighter",
        foreign_keys=[winner_id]
    )