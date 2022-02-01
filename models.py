import datetime as _dt
import sqlalchemy as _sql
import database as _db


class Movies(_db.Base):
    __tablename__ = "movies"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_sql.String, nullable=False, unique=True)
    release_year = _sql.Column(_sql.Integer)
    rating = _sql.Column(_sql.Float, default=5.0, nullable=False)
    duration = _sql.Column(_sql.Float, nullable=False)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)
