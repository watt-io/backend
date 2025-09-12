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
app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(router_film)
app.include_router(router_category)
app.include_router(router_director)
app.include_router(router_user)
