import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import env


DATABASE_URL = f"postgresql://myuser:password@localhost/movies_database"


engine = _sql.create_engine(DATABASE_URL)
print(engine)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
