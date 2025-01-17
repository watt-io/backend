from fastapi import FastAPI, HTTPException, Request
from app.models import Filme
from app.crud import listar_filmes, criar_filme, obter_filme_por_id

app = FastAPI()


@app.get("/filmes")
def get_filmes():
    filmes = listar_filmes()
    return [filme.to_dict() for filme in filmes]


@app.post("/filmes")
def post_filme(request: Request):
    data = request.json()  # Dados recebidos no corpo da requisição
    try:
        novo_filme = Filme(
            id=data["id"],
            titulo=data["titulo"],
            diretor=data["diretor"],
            ano=data["ano"],
        )
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Campo obrigatório ausente: {e}")
    return criar_filme(novo_filme).to_dict()


@app.get("/filmes/{id}")
def get_filme_por_id(id: int):
    filme = obter_filme_por_id(id)
    if filme:
        return filme.to_dict()
    raise HTTPException(status_code=404, detail="Filme não encontrado")
