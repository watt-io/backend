from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a file in the same directory as we're working on
# Calling it "sql_server.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_server.db"

# Engine, session and base are the objects that will make the "connection"
# with the server (where base is the one we'll use for 'create table')
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()