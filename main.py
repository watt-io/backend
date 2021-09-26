# Projeto API REST para um catálogo de filmes
# Autor :  Gabriel Orlando Campista Petrucci
# Projeto realizado utilizando a documentação em https://fastapi.tiangolo.com/tutorial

from fastapi import FastAPI, Request, Depends
from sqlalchemy.orm import Session
from movies import Movies

# Libs to create a template
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# Importing tableModel to start DB
import tableModel
from tableModel import MoviesTable 
# Importing Engine and Session from .database
from database import engine, SessionLocal
tableModel.Base.metadata.create_all(bind = engine)



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
# Database Dependency - Once the request was made, it will proceed to finish it (as well as the SessionLocal)
# and then, it will create another session (if there's another request)
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        # Garanteed the session will be closed after request is done
        db.close()
        
# Root path - Visual interface (HTML using jinja2)
@app.get("/", response_class=HTMLResponse)
def root(request:Request , db: Session = Depends(get_db)):
    mvs = get_movies(db)
    return templates.TemplateResponse("index.html",{"request": request, "mv_table": mvs})

# Path - filmes [GET]
@app.get("/filmes")
def get_movies(db: Session = Depends(get_db)):
    return db.query(MoviesTable).all()
 

# Path - filmes [POST]
@app.post("/filmes")
def post_movies(movie : Movies , db : Session = Depends(get_db)):

    # Define what is going to be added to DB
    mv_table = MoviesTable(**movie.dict())
 
    # Add it
    db.add(mv_table)
    db.commit()
    db.refresh
    
    return {"Mensagem": "Filme {0} cadastrado!".format(movie.name)}
    

# Path - filmes/{id} 
@app.get("/filmes/{id}")
def getById(id : int , db: Session = Depends(get_db)):
    # Search for movies with specified ID, if it exists -> return the first found
    # if it doesn't, return an error message
    mv = db.query(MoviesTable).filter(MoviesTable.id == id).first()
    if mv is None:
        return {"Erro": "ID não encontrado!"}
    return mv

    