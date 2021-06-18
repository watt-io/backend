from app.api.models import FilmeSchema
from app.db import filmes, database


async def post(payload: FilmeSchema):
    query = filmes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)


async def get(id: int):
    query = filmes.select().where(id == filmes.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = filmes.select()
    return await database.fetch_all(query=query)
