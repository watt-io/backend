from datetime import date
from Models.CategoryModel import Category
from Models.DirectorModel import Director
from Models.FilmModel import Film
from random import choice, randint, uniform
from faker import Faker

fake = Faker()

def seed_data(db):
    # ---------- CATEGORIES ----------
    categories = ["Action", "Funny", "Drama", "Horror"]
    for name in categories:
        if not db.query(Category).filter_by(name=name).first():
            db.add(Category(name=name))
    db.commit()

    # ---------- DIRECTORS ----------
    for _ in range(5):
        name = fake.name()
        nationality = fake.country()
        birth_date = fake.date_of_birth(minimum_age=30, maximum_age=80)
        if not db.query(Director).filter_by(name=name).first():
            db.add(Director(name=name, nationality=nationality, birth_date=birth_date))
    db.commit()

  

    # ---------- FILMS ----------
    categories_db = db.query(Category).all()
    directors_db = db.query(Director).all()

    for _ in range(10):
        title = fake.sentence(nb_words=3)
        synopsis = fake.text(max_nb_chars=200)
        duration = randint(80, 180)
        language = choice(["English", "Portuguese", "Spanish", "French"])
        release_year = randint(1900, 2025)
        rating = round(uniform(5.0, 10.0), 1)
        category_id = choice(categories_db).id
        director_id = choice(directors_db).id

        if not db.query(Film).filter_by(title=title).first():
            db.add(Film(
                title=title,
                synopsis=synopsis,
                duration=duration,
                language=language,
                release_year=release_year,
                rating=rating,
                category_id=category_id,
                director_id=director_id
            ))

    db.commit()
    print("Seeds criadas com sucesso!")
