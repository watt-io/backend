from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_user
from app.database import get_db
from app.repositories.filme_repository import FilmeRepository
from app.schemas.filme import FilmeCreate, FilmeResponse

router = APIRouter(prefix="/filmes", tags=["filmes"])


def get_filme_repository(
    session: AsyncSession = Depends(get_db),
) -> FilmeRepository:
    return FilmeRepository(session)


@router.get("", response_model=list[FilmeResponse])
async def listar_filmes(
    repository: FilmeRepository = Depends(get_filme_repository),
    _current_user: str = Depends(get_current_user),
) -> list[FilmeResponse]:
    filmes = await repository.list_all()
    return [FilmeResponse.model_validate(f) for f in filmes]


@router.post("", response_model=FilmeResponse, status_code=status.HTTP_201_CREATED)
async def criar_filme(
    filme: FilmeCreate,
    repository: FilmeRepository = Depends(get_filme_repository),
    _current_user: str = Depends(get_current_user),
) -> FilmeResponse:
    criado = await repository.create(filme)
    return FilmeResponse.model_validate(criado)


@router.get("/{filme_id}", response_model=FilmeResponse)
async def obter_filme(
    filme_id: int,
    repository: FilmeRepository = Depends(get_filme_repository),
    _current_user: str = Depends(get_current_user),
) -> FilmeResponse:
    filme = await repository.get_by_id(filme_id)
    if filme is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado",
        )
    return FilmeResponse.model_validate(filme)


@router.delete("/{filme_id}", status_code=status.HTTP_204_NO_CONTENT)
async def excluir_filme(
    filme_id: int,
    repository: FilmeRepository = Depends(get_filme_repository),
    _current_user: str = Depends(get_current_user),
) -> None:
    deleted = await repository.delete(filme_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado",
        )
