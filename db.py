import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
engine = sqlalchemy.create_engine('sqlite:///filmes.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)

def get_db():
    db = Session()
    try:
        yield db

    finally:
        db.close()
