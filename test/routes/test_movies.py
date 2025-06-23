from http import HTTPStatus
from typing import Any

from fastapi.testclient import TestClient


def test_create_movie(client: TestClient, movie_payload: dict[str, Any]) -> None:
    response = client.post('/filmes', json=movie_payload)
    data = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert data['title'] == movie_payload['title']
    assert data['overview'] == movie_payload['overview']
    assert data['year'] == movie_payload['year']
    assert data['rating'] == movie_payload['rating']
    assert data['category'] == movie_payload['category']
    assert 'id' in data


def test_create_movie_with_invalid_payload(client: TestClient) -> None:
    response = client.post('/filmes', json={})
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_get_movies(client: TestClient) -> None:
    response = client.get('/filmes')
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert isinstance(data, list)
    assert len(data) > 0
    assert all('id' in movie for movie in data)
    assert all('title' in movie for movie in data)
    assert all('overview' in movie for movie in data)
    assert all('year' in movie for movie in data)
    assert all('rating' in movie for movie in data)
    assert all('category' in movie for movie in data)


def test_get_movie_by_id(client: TestClient, movie_payload: dict[str, Any]) -> None:
    response = client.get('/filmes/1')
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data['id'] == 1
    assert data['title'] == movie_payload['title']
    assert data['overview'] == movie_payload['overview']
    assert data['year'] == movie_payload['year']
    assert data['rating'] == movie_payload['rating']
    assert data['category'] == movie_payload['category']


def test_get_movie_with_invalid_id(client: TestClient) -> None:
    response = client.get('/filmes/999')
    data = response.json()

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert data['detail'] == 'Movie not found'
