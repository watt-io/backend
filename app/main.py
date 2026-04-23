from fastapi import FastAPI
from app.database import engine, Base
from app.routers import filmes
from app.logger import get_logger

logger = get_logger(__name__)

# Cria as tabelas no banco de dados (SQLite) na inicialização.
# Em projetos grandes, usariamos ferramentas de migração como Alembic,
# mas para este desafio, essa abordagem é suficiente e prática.
logger.info("Inicializando banco de dados...")
Base.metadata.create_all(bind=engine)

# Instancia a aplicação FastAPI, definindo título e descrição para o Swagger
app = FastAPI(
    title="API de Filmes",
    description="Desafio Técnico - CRUD de Filmes utilizando FastAPI e SQLAlchemy.",
    version="1.0.0"
)

# Inclui as rotas do módulo de filmes na aplicação principal
app.include_router(filmes.router)

@app.get("/")
def root():
    """Rota raiz apenas para verificar se a API está no ar."""
    return {"message": "API de Filmes está rodando. Acesse /docs para a documentação."}