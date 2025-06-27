from adapters.driven.database.connection import engine
from adapters.driven.database.models import Base

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")