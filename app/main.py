from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import engine, Base
from app.models.filme import Movie
from app.models.usuario import User
from app.routes import auth, filmes as movies, usuarios as users

# As tabelas serão criadas via Alembic migrations
# Base.metadata.create_all(bind=engine)

# Criar aplicação FastAPI
app = FastAPI(
    title="WATT Movies API",
    description="REST API for movie management with JWT authentication",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.router)
app.include_router(movies.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    """API root endpoint"""
    return {
        "message": "Welcome to WATT Movies API!",
        "docs": "/docs",
        "redoc": "/redoc",
    }


@app.get("/health")
def health_check():
    """API health check"""
    return {"status": "healthy", "message": "API is running normally"}
