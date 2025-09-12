from fastapi import FastAPI
from Data.session import Base, engine
from Models.CategoryModel import Category
from Models.DirectorModel import Director
from Models.FilmModel import Film
from Models.UserModel import User
from Controllers.FilmController import router_film
from Controllers.CategoryController import router_category
from Controllers.DirectorController import router_director
from Controllers.UserController import router_user

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Lista de domínios de exemplo que podem acessar nosso backend
origins = [
    "http://localhost:3000",  # React dev
    "https://meusite.com.br", # Produção
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Permitir apenas esses domínios
    allow_credentials=True,     # Permite enviar cookies ou auth headers
    allow_methods=["*"],        # Permite todos os métodos HTTP (GET, POST, etc)
    allow_headers=["*"],        # Permite todos os headers
)

app.include_router(router_film)
app.include_router(router_category)
app.include_router(router_director)
app.include_router(router_user)
