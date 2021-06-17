from fastapi.testclient import TestClient
from api.routes.film_v1 import router
from main import app

client = TestClient(app)

auth_token = None
film_id = 1

def test_login():
    global auth_token
    response = client.post(
        '/auth/token/',
        headers={'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
        data={'username': 'admin', 'password': 'admin'}
    )
    assert response.status_code == 200
    auth_token = response.json().get('access_token')


def test_create_film():
    global film_id
    response = client.post(
        '/filmes/',
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {auth_token}'
        },
        json={'title': 'The Thing', 'director': 'John Carpenter', 'release_on': '1982-02-03'},
    )
    assert response.status_code == 200
    film_id = response.json().get('id')


def test_read_all_films():
    response = client.get(
        '/filmes/', 
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {auth_token}'
        },
    )
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_read_film():
    response = client.get(
        f'/filmes/{film_id}',
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {auth_token}'
        },
    )
    assert response.status_code == 200


def test_update_film():
    response = client.put(
        f'/filmes/{film_id}',
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {auth_token}'
        },
        json={'title': 'The Shining', 'director': 'Stanley Kubrick', 'release_on': '1980-12-25'},
    )
    assert response.status_code == 200


def test_delete_film():
    # ! Deletar filme recem criado durante a exec deste teste
    client.delete(
        f'/filmes/{film_id}',
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {auth_token}'
        },
    )
    response = client.get(
        f'/filmes/{film_id}',
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {auth_token}'
        },
    )
    assert response.status_code == 200
    assert response.json() == None