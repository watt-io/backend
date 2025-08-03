import pytest
from unittest.mock import patch, MagicMock
from fastapi import status
from app.models.filme import Movie


class TestMoviesRoutes:

    def test_get_movies_empty(self, client):
        response = client.get("/movies")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data == []

    def test_get_movies_with_data(self, client, db_session, mock_movie):
        db_session.add(mock_movie)
        db_session.commit()

        response = client.get("/movies")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 1
        assert data[0]["title"] == mock_movie.title
        assert data[0]["year"] == mock_movie.year

    def test_get_movies_pagination(self, client, db_session):
        movies = []
        for i in range(5):
            movie = Movie(
                id=i + 1,
                title=f"Movie {i+1}",
                year=2020 + i,
                director=f"Director {i+1}",
                genre="Action",
                synopsis=f"Synopsis {i+1}",
                duration=120,
                rating=8.0,
            )
            movies.append(movie)
            db_session.add(movie)
        db_session.commit()

        response = client.get("/movies?limit=3")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 3

        response = client.get("/movies?skip=2&limit=2")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 2
        assert data[0]["title"] == "Movie 3"

    def test_get_movie_by_id_success(self, client, db_session, mock_movie):
        db_session.add(mock_movie)
        db_session.commit()

        response = client.get(f"/movies/{mock_movie.id}")

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == mock_movie.id
        assert data["title"] == mock_movie.title

    def test_get_movie_by_id_not_found(self, client):
        response = client.get("/movies/999")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "Movie not found" in response.json()["detail"]

    def test_create_movie_success(
        self, client, db_session, mock_user, headers_auth, movie_create_data
    ):
        db_session.add(mock_user)
        db_session.commit()

        response = client.post("/movies", json=movie_create_data, headers=headers_auth)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["title"] == movie_create_data["title"]
        assert data["year"] == movie_create_data["year"]
        assert "id" in data

    def test_create_movie_unauthorized(self, client, movie_create_data):
        response = client.post("/movies", json=movie_create_data)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_movie_invalid_data(
        self, client, db_session, mock_user, headers_auth
    ):
        db_session.add(mock_user)
        db_session.commit()

        response = client.post(
            "/movies",
            json={"title": "", "year": "year_invalid"},
            headers=headers_auth,
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_update_movie_success(
        self, client, db_session, mock_movie, mock_user, headers_auth
    ):

        db_session.add(mock_movie)
        db_session.add(mock_user)
        db_session.commit()

        update_data = {"title": "Interstellar (Updated)", "rating": 9.0}

        response = client.put(
            f"/movies/{mock_movie.id}", json=update_data, headers=headers_auth
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["title"] == update_data["title"]
        assert data["rating"] == update_data["rating"]

    def test_update_movie_not_found(
        self, client, db_session, mock_user, headers_auth
    ):

        db_session.add(mock_user)
        db_session.commit()

        response = client.put(
            "/movies/999", json={"title": "New Title"}, headers=headers_auth
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "Movie not found" in response.json()["detail"]

    def test_update_movie_unauthorized(self, client, db_session, mock_movie):
        db_session.add(mock_movie)
        db_session.commit()

        response = client.put(
            f"/movies/{mock_movie.id}", json={"title": "New Title"}
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_movie_success(
        self, client, db_session, mock_movie, mock_user, headers_auth
    ):
        db_session.add(mock_movie)
        db_session.add(mock_user)
        db_session.commit()

        response = client.delete(f"/movies/{mock_movie.id}", headers=headers_auth)

        assert response.status_code == status.HTTP_200_OK
        assert "Movie removed successfully" in response.json()["message"]

        get_response = client.get(f"/movies/{mock_movie.id}")
        assert get_response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_movie_not_found(
        self, client, db_session, mock_user, headers_auth
    ):
        db_session.add(mock_user)
        db_session.commit()

        response = client.delete("/movies/999", headers=headers_auth)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "Movie not found" in response.json()["detail"]

    def test_delete_movie_unauthorized(self, client, db_session, mock_movie):
        db_session.add(mock_movie)
        db_session.commit()

        response = client.delete(f"/movies/{mock_movie.id}")

        assert response.status_code == status.HTTP_403_FORBIDDEN
