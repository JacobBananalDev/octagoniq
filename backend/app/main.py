# Import FastAPI class from the fastapi library
from fastapi import FastAPI

# Create an instance of the FastAPI application
# This is the main entrypoint of our API
app = FastAPI()


# Define a simple GET route at the root URL "/"
# When someone visits http://localhost:8000/
# this function will run
@app.get("/")
def root():
    """
    Root endpoint.
    Used to verify that the API is running.
    """
    return {"message": "Welcome to OctagonIQ API"}