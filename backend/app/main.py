# Import FastAPI class from the fastapi library
from fastapi import FastAPI
from sqlalchemy import text
from app.models.fighter import Fighter
from app.models.event import Event
from app.models.fight import Fight
from app.models.user import User
from app.routes import fighter, event, fight, auth, user

# Create an instance of the FastAPI application
# This is the main entrypoint of our API
app = FastAPI()

# Create tables in the database (if they don't already exist)

app.include_router(fighter.router)
app.include_router(event.router)
app.include_router(fight.router)
app.include_router(auth.router)
app.include_router(user.router)

@app.on_event("startup")
def startup_event():
    """
    Development-only: ensure tables exist.
    In production, this should be handled via migrations.
    """
    from app.database import Base, engine
    Base.metadata.create_all(bind=engine)