#import datetime as _dt
import sqlalchemy as _sql
#import sqlalchemy.orm as _orm

import database as _database


class Filme(_database.Base):
    __tablename__ = "filmes"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    nome = _sql.Column(_sql.String, unique=True, index=True)
    ano = _sql.Column(_sql.Integer)
    diretor = _sql.Column(_sql.String)

