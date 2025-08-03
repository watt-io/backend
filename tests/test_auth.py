import pytest
from unittest.mock import patch, MagicMock
from fastapi import status
from app.models.usuario import User


class TestAuthRoutes:

    def test_register_success(self, client, usuario_create_data):

        response = client.post("/auth/register", json=usuario_create_data)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["email"] == usuario_create_data["email"]
        assert data["name"] == usuario_create_data["name"]
        assert "id" in data
        assert "password" not in data

    def test_register_duplicate_email(self, client, db_session, mock_usuario):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.post(
            "/auth/register",
            json={
                "email": mock_usuario.email,
                "password": "123456",
                "name": "Outro Usuário",
            },
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "Email already registered" in response.json()["detail"]

    def test_register_invalid_email(self, client):
        response = client.post(
            "/auth/register",
            json={"email": "email-invalido", "senha": "123456", "nome": "Usuário"},
        )

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_login_success(self, client, db_session, mock_usuario):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.post(
            "/auth/login", json={"email": mock_usuario.email, "password": "123456"}
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    def test_login_invalid_credentials(self, client, db_session, mock_usuario):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.post(
            "/auth/login", json={"email": mock_usuario.email, "password": "senha_errada"}
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "Incorrect email or password" in response.json()["detail"]

    def test_login_user_not_found(self, client):
        response = client.post(
            "/auth/login", json={"email": "naoexiste@exemplo.com", "password": "123456"}
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert "Incorrect email or password" in response.json()["detail"]

    def test_get_current_user_success(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.get("/auth/me", headers=headers_auth)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["email"] == mock_usuario.email
        assert data["name"] == mock_usuario.name

    def test_get_current_user_invalid_token(self, client):
        response = client.get(
            "/auth/me", headers={"Authorization": "Bearer token_invalido"}
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_current_user_no_token(self, client):
        response = client.get("/auth/me")

        assert response.status_code == status.HTTP_403_FORBIDDEN
