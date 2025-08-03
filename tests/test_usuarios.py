import pytest
from unittest.mock import patch, MagicMock
from fastapi import status
from app.models.usuario import User


class TestUsuariosRoutes:

    def test_get_usuarios_empty(self, client, db_session, mock_usuario, headers_auth):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.get("/users", headers=headers_auth)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 1

    def test_get_usuarios_with_data(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)

        outro_usuario = User(
            id=2,
            email="outro@exemplo.com",
            password_hash="hash_senha",
            name="Outro Usuário",
        )
        db_session.add(outro_usuario)
        db_session.commit()

        response = client.get("/users", headers=headers_auth)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) == 2

    def test_get_usuarios_unauthorized(self, client):
        response = client.get("/users")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_get_usuario_by_id_success(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.get(f"/users/{mock_usuario.id}", headers=headers_auth)

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == mock_usuario.id
        assert data["email"] == mock_usuario.email

    def test_get_usuario_by_id_not_found(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.get("/users/999", headers=headers_auth)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "User not found" in response.json()["detail"]

    def test_get_usuario_by_id_unauthorized(self, client):
        response = client.get("/users/1")

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_usuario_success(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)
        db_session.commit()

        update_data = {"name": "Usuário Atualizado", "email": "atualizado@exemplo.com"}

        response = client.put(
            f"/users/{mock_usuario.id}", json=update_data, headers=headers_auth
        )

        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["name"] == update_data["name"]
        assert data["email"] == update_data["email"]

    def test_update_usuario_own_profile_only(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)

        outro_usuario = User(
            id=2,
            email="outro@exemplo.com",
            password_hash="hash_senha",
            name="Outro Usuário",
        )
        db_session.add(outro_usuario)
        db_session.commit()

        response = client.put(
            "/users/2", json={"name": "Hackeado"}, headers=headers_auth
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "You can only update your own profile" in response.json()["detail"]

    def test_update_usuario_duplicate_email(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)

        outro_usuario = User(
            id=2,
            email="outro@exemplo.com",
            password_hash="hash_senha",
            name="Outro Usuário",
        )
        db_session.add(outro_usuario)
        db_session.commit()

        response = client.put(
            f"/users/{mock_usuario.id}",
            json={"email": outro_usuario.email},
            headers=headers_auth,
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "Email already registered" in response.json()["detail"]

    def test_update_usuario_password(
        self, client, db_session, mock_usuario, headers_auth
    ):

        db_session.add(mock_usuario)
        db_session.commit()

        update_data = {"password": "nova_senha_123"}

        response = client.put(
            f"/users/{mock_usuario.id}", json=update_data, headers=headers_auth
        )

        assert response.status_code == status.HTTP_200_OK
        login_response = client.post(
            "/auth/login",
            json={"email": mock_usuario.email, "password": "nova_senha_123"},
        )
        assert login_response.status_code == status.HTTP_200_OK

    def test_update_usuario_not_found(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.put(
            "/users/999", json={"name": "Novo Nome"}, headers=headers_auth
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "You can only update your own profile" in response.json()["detail"]

    def test_update_usuario_unauthorized(self, client, db_session, mock_usuario):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.put(f"/users/{mock_usuario.id}", json={"name": "Novo Nome"})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_usuario_success(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.delete(f"/users/{mock_usuario.id}", headers=headers_auth)

        assert response.status_code == status.HTTP_200_OK
        assert "User removed successfully" in response.json()["message"]

        get_response = client.get(f"/users/{mock_usuario.id}", headers=headers_auth)
        assert get_response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_usuario_own_profile_only(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)

        outro_usuario = User(
            id=2,
            email="outro@exemplo.com",
            password_hash="hash_senha",
            name="Outro Usuário",
        )
        db_session.add(outro_usuario)
        db_session.commit()

        response = client.delete("/users/2", headers=headers_auth)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "You can only delete your own profile" in response.json()["detail"]

    def test_delete_usuario_not_found(
        self, client, db_session, mock_usuario, headers_auth
    ):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.delete("/users/999", headers=headers_auth)

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert "You can only delete your own profile" in response.json()["detail"]

    def test_delete_usuario_unauthorized(self, client, db_session, mock_usuario):
        db_session.add(mock_usuario)
        db_session.commit()

        response = client.delete(f"/users/{mock_usuario.id}")

        assert response.status_code == status.HTTP_403_FORBIDDEN
