from fastapi import FastAPI, Path, HTTPException, Depends # Importing framework for API use
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from Movie import *
from Client import * 
import Models


# Creating API ( uvicorn [File name]:[API Object name] --reload)
app = FastAPI()

# Creates a database and a table if it already not exists
Models.Base.metadata.create_all(bind = engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close



# Route Definition to define app functionalities
@app.get('/')
def homePage(db: Session = Depends(get_db)):
    return {"Filmes No Catálogo:" : db.query(Models.MovieDBModel).count()} # API works with Python dictionaries and translate to JSON format


@app.get('/filmes')
def getMovies(db: Session = Depends(get_db)):
    return db.query(Models.MovieDBModel).all()

@app.get('/filmes/{id}')
def getMovies(id: int = Path(None, description = 'O identificador do item que deseja consultar', gd = 0), db: Session = Depends(get_db)):
    getMovie = db.query(Models.MovieDBModel).filter(Models.MovieDBModel.id == id).first()
    if getMovie is None:
        # In a error case, a HTTP exception will be created to improve the communication with the user
        raise HTTPException(status_code=404,detail=f'Filme com a id: {id}, não está na lista')
    else:
        return getMovie # If movie Id is in the list, it returns the movie
    
@app.post('/filmes')
def postMovie(movie: MovieBase, db: Session = Depends(get_db)):
    # Create a new movie to be added and define movie Id as the last in the list
    newMovie = Models.MovieDBModel()
    newMovie.name = movie.movieName
    newMovie.length = movie.movieLength
    newMovie.genre = movie.movieGenre
    newMovie.release = movie.movieRelease
    
    db.add(newMovie)
    db.commit()
    
    return newMovie

@app.put('/filmes/{id}')
def updateMovie(movie: MovieBase, id: int = Path(None, description = 'O identificador do item que deseja alterar', gd = 0), db: Session = Depends(get_db)):
    newMovie = db.query(Models.MovieDBModel).filter(Models.MovieDBModel.id == id).first()
    if newMovie is None:
        raise HTTPException(status_code=404,detail=f'Filme com a id: {id}, não está na lista')
    else:
        newMovie.name = movie.movieName
        newMovie.length = movie.movieLength
        newMovie.genre = movie.movieGenre
        newMovie.release = movie.movieRelease
        db.add(newMovie)
        db.commit()
    
        return newMovie
    
@app.delete('/filmes/{id}')
def deleteMovie(id: int = Path(None, description = 'O identificador do item que deseja deletar', gd = 0), db: Session = Depends(get_db)):
    newMovie = db.query(Models.MovieDBModel).filter(Models.MovieDBModel.id == id).first()
    if newMovie is None:
        raise HTTPException(status_code=404,detail=f'Filme com a id: {id}, não está na lista')
    else:
        db.query(Models.MovieDBModel).filter(Models.MovieDBModel.id == id).delete()
        db.commit()
        return {"Filme Removido"}
    
@app.post('/alugar/{id}')
def rentMovie(client: ClientBase, id: int, db: Session = Depends(get_db)):
    rentMovie = db.query(Models.MovieDBModel).filter(Models.MovieDBModel.id == id).first()
    auxClient = db.query(Models.ClientDBModel).filter(Models.ClientDBModel.movie_id == id).first() #procura se alguém já alugou esse filme
    if rentMovie is None:
        raise HTTPException(status_code=404,detail=f'Filme com a id: {id}, não está na lista')
    elif auxClient is None:
        # Pydantic needs to know which key the variable provides a value to
        newClient = Models.ClientDBModel()
        newClient.name = client.clientName
        newClient.premiumAccount = client.clientPremium
        newClient.Adress = client.clientAdress
        newClient.movie_id = id
        db.add(newClient)
        db.commit()
        return db.query(Models.MovieDBModel).filter(Models.MovieDBModel.id == id).first()
    else:
        raise HTTPException(status_code=417,detail=f'Filme com a id: {id}, já foi alugado')

@app.delete('/Devolver/{id}')
def returnMovie(id: int, db: Session = Depends(get_db)):
    rentMovie = db.query(Models.MovieDBModel).filter(Models.MovieDBModel.id == id).first()
    returnClient = db.query(Models.ClientDBModel).filter(Models.ClientDBModel.movie_id == id).first()
    if rentMovie is None:
        raise HTTPException(status_code=404,detail=f'Filme com a id: {id}, não está na lista')
    elif returnClient is None:
        raise HTTPException(status_code=417,detail=f'O Filme com a id: {id}, não foi alugado')
    else:
        db.query(Models.ClientDBModel).filter(Models.ClientDBModel.movie_id == id).delete()
        db.commit()
        return {"Filme devolvido"}
        
@app.get('/clientes')
def getClients(db: Session = Depends(get_db)):
    return db.query(Models.ClientDBModel).all()

@app.get('/clientes/filmes')
def getClients(db: Session = Depends(get_db)):
    for cliente in db.query(Models.ClientDBModel).all():
        return cliente.filme