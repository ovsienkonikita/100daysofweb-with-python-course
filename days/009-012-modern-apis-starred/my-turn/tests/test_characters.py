import json

from requests import Response
from starlette.testclient import TestClient


def test_smoke(test_client):
    response: Response = test_client.get("/smoke")
    assert 200 == response.status_code


def test_get_characters(test_client):
    response: Response = test_client.get("/characters/")
    assert 200 == response.status_code
    data = response.json()
    assert data[0]["name"] == "Spider-Man"


def test_create_character(test_client: TestClient):
    data = {
        "pid": "999",
        "name": "Juice WRLD",
        "sex": "Male Characters",
        "sid": "da",
        "align": "adsas",
        "appearances": 999,
        "year": "2020",
    }
    response: Response = test_client.post("/characters/", json=data)
    assert response.status_code == 201
    assert data == response.json()


def test_get_single_character(test_client: TestClient):
    response: Response = test_client.get("/characters/2166")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Reed Richards"


def test_update_character(test_client: TestClient):
    data = {"name": "Capitan Ukraine"}
    response: Response = test_client.patch("/characters/7139", json=data)
    assert response.status_code == 200
    expected = {
        "align": "Good Characters",
        "appearances": 3360,
        "name": "Captain America",
        "pid": "7139",
        "sex": "Male Characters",
        "sid": "Public Identity",
        "year": "1941",
    }
    assert response.json() == expected


def test_delete_character(test_client: TestClient):
    response: Response = test_client.delete("/characters/7139")
    assert response.status_code == 204
    deleted_character_response: Response = test_client.get("/characters/7139")
    assert deleted_character_response.status_code == 404
