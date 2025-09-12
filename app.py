from fastapi import FastAPI
from Data.session import Base, engine
from Models.CategoryModel import Category
from Models.DirectorModel import Director
from Models.FilmModel import Film
from Models.UserModel import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

