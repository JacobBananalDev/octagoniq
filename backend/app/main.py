from fastapi import FastAPI

from app.routes import fighter, event, fight, auth, user

# Create FastAPI app instance
app = FastAPI()

# Register routers
app.include_router(fighter.router)
app.include_router(event.router)
app.include_router(fight.router)
app.include_router(auth.router)
app.include_router(user.router)
