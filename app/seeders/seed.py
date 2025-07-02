from app.core.database import SessionLocal, engine
from app.models.movie import Movie
from app.core.database import Base

def seed():
    Base.metadata.create_all(bind=engine)

    filmes = [
        {"name": "Dragon Ball Z: A Batalha dos Deuses", "description": "Goku enfrenta um novo deus da destruição", "genre": "Animação"},
        {"name": "O Máskara", "description": "Um homem tímido encontra uma máscara mágica que muda sua vida", "genre": "Comédia"},
        {"name": "Ace Ventura: Um Detetive Diferente", "description": "Um detetive excêntrico investiga desaparecimentos de animais", "genre": "Comédia"},
        {"name": "Homem-Aranha", "description": "Peter Parker ganha poderes aracnídeos e luta contra o crime", "genre": "Ação"},
    ]

    db = SessionLocal()
    try:
        for filme in filmes:
            exists = db.query(Movie).filter(Movie.name == filme["name"]).first()
            if not exists:
                novo_filme = Movie(**filme)
                db.add(novo_filme)

        db.commit()
        print('Filmes cadastrados com sucesso')
    finally:
        db.close()

if __name__ == '__main__':
    seed()
