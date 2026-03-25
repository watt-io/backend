import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app

# Banco de dados para testes
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

filme_exemplo = {
    "titulo": "O Poderoso Chefão",
    "diretor": "Francis Ford Coppola",
    "ano": 1972,
    "genero": "Drama"
}

# --- Tests ---

def test_criar_filme():
    response = client.post("/filmes", json=filme_exemplo)
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == filme_exemplo["titulo"]
    assert "id" in data

def test_criar_filme_sem_titulo():
    filme_invalido = {"diretor": "Alguém", "ano": 2020, "genero": "Ação"}
    response = client.post("/filmes", json=filme_invalido)
    assert response.status_code == 422

def test_listar_filmes_vazio():
    response = client.get("/filmes")
    assert response.status_code == 200
    assert response.json() == []

def test_listar_filmes():
    client.post("/filmes", json=filme_exemplo)
    client.post("/filmes", json={**filme_exemplo, "titulo": "Scarface"})
    response = client.get("/filmes")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_filtrar_por_genero():
    client.post("/filmes", json=filme_exemplo)
    client.post("/filmes", json={**filme_exemplo, "titulo": "Matrix", "genero": "Ficção"})
    response = client.get("/filmes", params={"genero": "Drama"})
    assert response.status_code == 200
    assert len(response.json()) == 1

def test_buscar_filme_por_id():
    criar = client.post("/filmes", json=filme_exemplo)
    filme_id = criar.json()["id"]
    response = client.get(f"/filmes/{filme_id}")
    assert response.status_code == 200
    assert response.json()["titulo"] == filme_exemplo["titulo"]

def test_buscar_filme_inexistente():
    response = client.get("/filmes/999")
    assert response.status_code == 404

def test_atualizar_filme():
    criar = client.post("/filmes", json=filme_exemplo)
    filme_id = criar.json()["id"]
    response = client.put(f"/filmes/{filme_id}", json={"titulo": "O Poderoso Chefão II"})
    assert response.status_code == 200
    assert response.json()["titulo"] == "O Poderoso Chefão II"

def test_deletar_filme():
    criar = client.post("/filmes", json=filme_exemplo)
    filme_id = criar.json()["id"]
    response = client.delete(f"/filmes/{filme_id}")
    assert response.status_code == 204
    assert client.get(f"/filmes/{filme_id}").status_code == 404

