from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas
from app.database import get_db
from app.logger import get_logger

# Instancia o logger para este módulo
logger = get_logger(__name__)

# Cria o roteador com um prefixo padrão e agrupa na documentação sob a tag "Filmes"
router = APIRouter(prefix="/filmes", tags=["Filmes"])

@router.get("/", response_model=List[schemas.FilmeResponse])
def listar_filmes(db: Session = Depends(get_db)):
    """
    Retorna todos os filmes cadastrados.
    Utiliza injeção de dependência para pegar a sessão do banco (db).
    """
    logger.info("Requisicao recebida para listar todos os filmes.")
    # Faz uma consulta no banco retornando todos os registros da tabela Filme
    filmes = db.query(models.Filme).all()
    return filmes

@router.post("/", response_model=schemas.FilmeResponse, status_code=status.HTTP_201_CREATED)
def cadastrar_filme(filme: schemas.FilmeCreate, db: Session = Depends(get_db)):
    """
    Cadastra um novo filme.
    Recebe os dados validados pelo schema FilmeCreate e retorna status 201 (Created).
    """
    logger.info(f"Tentando cadastrar o filme: {filme.titulo}")
    
    # Converte os dados recebidos (Pydantic) em um objeto do banco de dados (SQLAlchemy)
    novo_filme = models.Filme(**filme.model_dump())
    
    try:
        # Adiciona a transação na sessão
        db.add(novo_filme)
        # Confirma (salva) a transação no banco de dados
        db.commit()
        # Atualiza o objeto com os dados gerados pelo banco (como o ID)
        db.refresh(novo_filme)
        
        logger.info(f"Filme cadastrado com sucesso. ID: {novo_filme.id}")
        return novo_filme
    except Exception as e:
        # Em caso de erro, desfaz qualquer alteração pendente e levanta exceção HTTP
        db.rollback()
        logger.error(f"Erro ao cadastrar filme: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno ao tentar salvar o filme."
        )

@router.get("/{id}", response_model=schemas.FilmeResponse)
def buscar_filme_por_id(id: int, db: Session = Depends(get_db)):
    """
    Busca um filme específico pelo ID.
    Retorna erro 404 caso o filme não exista.
    """
    logger.info(f"Buscando filme com ID: {id}")
    
    # Consulta buscando o primeiro registro que coincida com o ID passado
    filme = db.query(models.Filme).filter(models.Filme.id == id).first()
    
    if not filme:
        logger.warning(f"Filme com ID {id} nao encontrado.")
        # Se não encontrar, retorna erro padronizado para o cliente
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Filme não encontrado."
        )
        
    return filme