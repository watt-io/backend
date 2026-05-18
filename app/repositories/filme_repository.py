from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.filme import Filme
from app.schemas.filme import FilmeCreate


class FilmeRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def list_all(self) -> list[Filme]:
        result = await self.session.execute(select(Filme).order_by(Filme.id))
        return list(result.scalars().all())

    async def get_by_id(self, filme_id: int) -> Filme | None:
        return await self.session.get(Filme, filme_id)

    async def create(self, data: FilmeCreate) -> Filme:
        filme = Filme(**data.model_dump())
        self.session.add(filme)
        await self.session.commit()
        await self.session.refresh(filme)
        return filme

    async def delete(self, filme_id: int) -> bool:
        filme = await self.get_by_id(filme_id)
        if filme is None:
            return False
        await self.session.delete(filme)
        await self.session.commit()
        return True
