from typing import Dict, Generator
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import random
import string
from app.core.config import settings
from app.main import app
from app import crud


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=10))


def random_email() -> str:
    return random_lower_string()


def test_create_user_return_201(client: TestClient, db: Session) -> None:

    username = random_lower_string()
    password = random_lower_string()
    data = {"username": username, "password": password}


    response = client.post(
        f"{settings.API_V1_STR}/users/", json=data,
    )

    created_user = response.json()
    user = crud.user.get_by_username(db, username=username)
    crud.user.remove(db=db, id=user.id)

    assert response.status_code == 201
    assert user
    assert user.username == created_user["username"]


def test_create_user_existing_username_return_400(
    client: TestClient, db: Session
) -> None:

    username = random_lower_string()
    password = random_lower_string()
    data = {"username": username, "password": password}


    response = client.post(
        f"{settings.API_V1_STR}/users/", json=data,
    )

    # post again with that username again!
    response = client.post(
        f"{settings.API_V1_STR}/users/", json=data,
    )

    created_user = response.json()

    assert response.status_code == 400
    assert "_id" not in created_user



