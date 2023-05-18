from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.core.config import settings
from app import crud 
import random
import string

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=10))


def random_username() -> str:
    return random_lower_string()


def test_get_access_token_return_200(db: Session, client: TestClient) -> None:

    username = random_lower_string()
    password = random_lower_string()
    data = {"username": username, "password": password}

    response_user_creation = client.post(
        f"{settings.API_V1_STR}/users/", json=data,
    )
    
    login_data = {
        "username": username,
        "password": password,
    }

    response = client.post(f"{settings.API_V1_STR}/login", data=login_data)
    tokens = response.json()
    assert response.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


def test_invalid_credentials_return_400(db: Session, client: TestClient) -> None:

    username = random_lower_string()
    password = random_lower_string()
    data = {"username": username, "password": password}

    response_user_creation = client.post(
        f"{settings.API_V1_STR}/users/", json=data,
    )
    
    login_data = {
        "username": username + 'x',
        "password": password,
    }

    response = client.post(f"{settings.API_V1_STR}/login", data=login_data)
    tokens = response.json()
    assert response.status_code == 400
    assert "access_token" not in tokens

