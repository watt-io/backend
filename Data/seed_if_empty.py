from Models.CategoryModel import Category
from Models.DirectorModel import Director
from Models.FilmModel import Film
from Models.UserModel import User
from Data.session import SessionLocal, Base
from Data.seeds import seed_data 

def seed_if_empty():
    db = SessionLocal()
    try:
        # Verifica se alguma tabela principal está vazia
        empty_category = db.query(Category).first() is None
        empty_director = db.query(Director).first() is None
        empty_film = db.query(Film).first() is None

        if empty_category or empty_director or empty_film:
            print("Banco vazio. Criando seeds...")
            seed_data(db)  # Passa a sessão para a função seed_data
        else:
            print("Banco já possui dados. Seeds não serão criadas.")
    finally:
        db.close()
