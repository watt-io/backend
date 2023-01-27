from fastapi import FastAPI, Path # Importing framework for API use
from pydantic import BaseModel
from Movie import * 
from Client import * 


# Creating API ( uvicorn [File name]:[API Object name] --reload)
app = FastAPI()

# Dictionary with movies in DB 
movie1 = Movie(0)
movie1.setMovieName('Harry Potter e a Pedra Filosofal')
movie1.setMovieGenre('Fantasia/Aventura')
movie1.setMovieLength('152 minutos')
movie1.setMovieRelease('2001')
movie1.setMovieRentedBy({'Antônio Carlos', False, 'Avenida Brasil 456'})

movie2 = Movie(1)
movie2.setMovieName('Harry Potter e a Câmara Secreta')
movie2.setMovieGenre('Fantasia/Aventura')
movie2.setMovieLength('161 minutos')
movie2.setMovieRelease('2002')



movies = {
    movie1.getMovieId(): movie1,
    movie2.getMovieId(): movie2
}


# Route Definition to define app functionalities



@app.get('/')
def homePage():
    return {'Filmes No Catálogo:' : len(movies)} # API works with Python dictionaries and translate to JSON format


@app.get('/filmes')
def getMovies():
    for movie in movies:
        return movies

@app.get('/filmes/{id}')
def getmovies(id: int = Path(None, description = 'O identificador do item que deseja consultar', gd = 0)):
    if(id in movies):
        return movies[id] # If movie Id is in the list, it returns the movie
    else:
        return {'Filme não está na lista'}
    
@app.post('/filmes')
def postMovie(name: str = Path(description = 'Nome do Filme'), length: str = Path(description = ' Valor da duração em minutos do filme'), genre: str = Path(description = 'Genero do Filme'), release: str = Path(description = 'Ano de estréia do Filme')):
    # Create a new movie to be added 
    newMovie = Movie(len(movies)) # Define movie Id as the last in the list
    newMovie.setMovieName(name)
    newMovie.setMovieGenre(genre)
    newMovie.setMovieLength(length)
    newMovie.setMovieRelease(release)
    movies[newMovie.getMovieId()] = newMovie
    
@app.put('/alugar/{id}')
def rentMovie(client: Client, id: int):
    if(id not in movies):
        return {'Filme não está na lista'}
    elif(movies[id].getMovieRentedBy() == None):
        # Pydantic needs to know which key the variable provides a value to
        newClient = Client(clientName = client.clientName, clientPremium= client.clientPremium, clientAdress = client.clientAdress) 
        movies[id].setMovieRentedBy(newClient)
        return movies[id]
    else:
        return {'Filme já alugado'}

@app.put('/Devolver/{id}')
def returnMovie(id: int):
    if(id not in movies):
        return {'Filme não está na lista'}
    elif(movies[id].getMovieRentedBy() == None):
        return {'Filme não foi alugado'}
    else:
        movies[id].setMovieRentedBy(None)
        return {'Filme Devolvido'}
        

