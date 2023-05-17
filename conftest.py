from typing import Generator
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import SessionLocal 
import pytest
from app.models import User
from app.core.config import settings

@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def authenticated_client():
    auth_client = TestClient(app)

    data = {"username": "auth_user", "password": "auth_user_password"}

    auth_client.post(f"{settings.API_V1_STR}/users/", json=data)

    response = auth_client.post(f"{settings.API_V1_STR}/login", data=data)
    tokens = response.json()

    return auth_client, tokens, data