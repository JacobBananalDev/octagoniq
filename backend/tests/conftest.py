import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app as fastapi_app
from app.database import Base
from app.database import get_db  # <-- adjust if needed
from app.core.settings import settings
# Force model imports
import app.models

engine = create_engine(settings.DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

@pytest.fixture(autouse=True)
def setup_test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield

@pytest.fixture()
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

@pytest.fixture()
def client(db_session):
    def override_get_db():
        yield db_session

    fastapi_app.dependency_overrides[get_db] = override_get_db

    with TestClient(fastapi_app) as c:
        yield c

    fastapi_app.dependency_overrides.clear()
    
#  AUTH FIXTURES
    
@pytest.fixture()
def create_admin_user(db_session):
    from app.models.user import User
    from app.core.security import hash_password

    admin = User(
        username="admintest",
        email="admin@test.com",
        hashed_password=hash_password("StrongPassword123!"),
        role="admin",  # 👈 critical
        is_active=True
    )

    db_session.add(admin)
    db_session.commit()
    db_session.refresh(admin)

    return admin


@pytest.fixture()
def admin_token(client, create_admin_user):
    login_data = {
        "username": "admintest",
        "password": "StrongPassword123!"
    }

    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200

    return response.json()["access_token"]


