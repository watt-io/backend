from fastapi import APIRouter

routes = APIRouter(prefix="/filmes", tags=['Filmes'])

@routes.get('/')
async def getFilmes():
    """
    Rota padrão para listagem de filmes.
    """
    return {"mensagem": "obtendo filmes"}

@routes.post('/')
async def createdFilmes():
    """
    Rota padrão para a criação de filmes.
    """
    pass

@routes.get(f"/{id}")
async def getFilmeById(id: int):
    """
    Rota padrão para a obter um filme pelo seu ID
    """
    return {"mensagem": f"obtendo filme {id}"}