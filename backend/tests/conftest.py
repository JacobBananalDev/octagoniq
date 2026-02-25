import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.database import Base
from app.database import get_db  # <-- adjust if needed
from app.core.dependencies import require_admin
from app.models.user import User

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def db_session():
    connection = engine.connect()
    transaction = connection.begin()

    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture()
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()
    
#  AUTH FIXTURES
    
@pytest.fixture()
def create_admin_user(client):
    payload = {
        "username": "admintest",
        "email": "admin@example.com",
        "password": "StrongPassword123!",
    }

    response = client.post("/auth/register", json=payload)
    assert response.status_code == 201

    return payload


@pytest.fixture()
def admin_token(client, create_admin_user):
    login_data = {
        "username": create_admin_user["username"],
        "password": create_admin_user["password"]
    }

    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200

    return response.json()["access_token"]


