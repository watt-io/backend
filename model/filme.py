from sqlalchemy import Table, Column
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String

filmes = Table(
    'filmes',meta,
    Column('id',Integer,primary_key=True),
    Column('nome',String(255)),
    Column('genero',String(255)),
    Column('diretor',String(255))
)

