import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import database as _database


class Movies(_database.Base):
    __tablename__ = "Filmes"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String, nullable=False, unique=True)
    genre = _sql.Column(_sql.String, nullable=False)
    release = _sql.Column(_sql.Integer)