# Import FastAPI class from the fastapi library
from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine

# Create an instance of the FastAPI application
# This is the main entrypoint of our API
app = FastAPI()


# Define a simple GET route at the root URL "/"
# When someone visits http://localhost:8000/
# this function will run
@app.get("/")
def root():
   # Test DB connection
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"db_status": result.scalar()}