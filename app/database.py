from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_engine(settings.database_url)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()
