from app.core.config import settings
from fastapi import status
import datetime
import random
import string

from app import crud

def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=10))


def random_username() -> str:
    return random_lower_string()


def test_get_all_conferences_return_200(authenticated_client):
    auth_client, tokens, data = authenticated_client
    header = {
        "Authorization": "Bearer " + tokens["access_token"]
    }

    response = auth_client.get(f"{settings.API_V1_STR}/conferences", headers=header)

    assert response.status_code == status.HTTP_200_OK


def test_post_a_conferences_return_201(authenticated_client):

    auth_client, tokens, data = authenticated_client
    header = {
        "Authorization": "Bearer " + tokens["access_token"]
    }
    conference = {
        "title": random_lower_string(),
        "description": random.choice([None]+[random_lower_string()]), 
        "start_time": "2023-05-18T07:06:07.808000",
        "end_time": "2023-05-18T07:06:07.808000",
        "Capacity": random.randint(1, 50) 
    }

    response = auth_client.post(f"{settings.API_V1_STR}/conferences", json=conference, headers=header)
    assert response.status_code == status.HTTP_201_CREATED
    # because ConferenceIn and ConferenceOut are similar ins schemas
    assert response.json()["title"] == conference["title"]


def test_delete_a_conferences_return_204(authenticated_client):

    auth_client, tokens, data = authenticated_client
    header = {
        "Authorization": "Bearer " + tokens["access_token"]
    }
    conference = {
        "title": random_lower_string(),
        "description": random.choice([None]+[random_lower_string()]), 
        "start_time": "2023-05-18T07:06:07.808000",
        "end_time": "2023-05-18T07:06:07.808000",
        "Capacity": random.randint(1, 50) 
    }

    response = auth_client.post(f"{settings.API_V1_STR}/conferences", json=conference, headers=header)
    json_response = response.json()
    conference_id = int(json_response["id"])
    response = auth_client.delete(f"{settings.API_V1_STR}/conferences/{conference_id}", headers=header)

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_update_a_conferences_return_200(authenticated_client):

    auth_client, tokens, data = authenticated_client
    header = {
        "Authorization": "Bearer " + tokens["access_token"]
    }
    conference = {
        "title": random_lower_string(),
        "description": random.choice([None]+[random_lower_string()]), 
        "start_time": "2023-05-18T07:06:07.808000",
        "end_time": "2023-05-18T07:06:07.808000",
        "Capacity": random.randint(1, 50) 
    }

    response = auth_client.post(f"{settings.API_V1_STR}/conferences", json=conference, headers=header)
    json_response = response.json()
    conference_id = int(json_response["id"])

    conference_updated = {
        "title": random_lower_string(),
        "description": random.choice([None]+[random_lower_string()]), 
        "start_time": "2023-05-18T07:06:07.808000",
        "end_time": "2023-05-18T07:06:07.808000",
        "Capacity": random.randint(1, 50) 
    }

    response = auth_client.put(f"{settings.API_V1_STR}/conferences/{conference_id}", json=conference_updated, headers=header)
    print(response)
    print(response.json())
    assert response.status_code == status.HTTP_200_OK