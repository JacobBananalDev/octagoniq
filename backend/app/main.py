# Import FastAPI class from the fastapi library
from fastapi import FastAPI
from sqlalchemy import text
from app.database import Base, engine
from app.models.fighter import Fighter
from app.models.event import Event
from app.models.fight import Fight
from app.models.user import User
from app.routes import fighter, event, fight, auth

# Create an instance of the FastAPI application
# This is the main entrypoint of our API
app = FastAPI()

# Create tables in the database (if they don't already exist)
Base.metadata.create_all(bind=engine)

app.include_router(fighter.router)
app.include_router(event.router)
app.include_router(fight.router)
app.include_router(auth.router)


# Define a simple GET route at the root URL "/"
# When someone visits http://localhost:8000/
# this function will run
@app.get("/")
def root():
   # Test DB connection
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"db_status": result.scalar()}