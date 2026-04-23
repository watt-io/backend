from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL de conexão. O prefixo 'sqlite:///' indica um banco de dados local em arquivo.
SQLALCHEMY_DATABASE_URL = "sqlite:///./filmes.db"

# Cria o 'motor' do SQLAlchemy. 
# connect_args={"check_same_thread": False} é necessário apenas para SQLite no FastAPI.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria a fábrica de sessões. Cada requisição na API terá sua própria sessão isolada.
# autocommit=False e autoflush=False garantem que nós controlaremos quando salvar os dados.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base que servirá de herança para todos os nossos modelos de banco de dados.
Base = declarative_base()

def get_db():
    """
    Dependency Injection (Injeção de Dependência) para obter a sessão do banco.
    Motivo: Garante que cada requisição receba uma conexão limpa e que essa conexão
    seja encerrada adequadamente após o uso, evitando vazamento de memória.
    """
    db = SessionLocal()
    try:
        # O 'yield' pausa a função e entrega a sessão para o endpoint usar
        yield db
    finally:
        # Independentemente de sucesso ou erro no endpoint, a sessão é fechada
        db.close()