from fastapi import FastAPI, Path, Query, Body, Depends, HTTPException
from typing import Optional, List, Dict, Annotated
from models import Film, Base
from schemas import FilmBase, FilmSQLBase, AllFilmsWithPagination, AllFilms, ChromaQuery, ChromaQueryFilmsList
from database import engine, session_local
from sqlalchemy.orm import Session
from for_chromaDB.chromaDBService import ChromaDBService

app = FastAPI()
Base.metadata.create_all(bind=engine)
chroma_service = ChromaDBService()

def get_sql_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.get("/films/")
async def get_films(db: Session = Depends(get_sql_db)) -> AllFilms:
    query = db.query(Film).order_by("vote_average")
    results = query.all()
    films = [FilmSQLBase.model_validate(film) for film in results]

    return AllFilms(films=films)

@app.get("/films/search/{title}")
async def get_film_by_title(title: Annotated[str, Path(example="Interstellar", min_length=1, max_length=100)], db: Session = Depends(get_sql_db)) -> FilmSQLBase:
    film = db.query(Film).filter(Film.title == title).first()
    if not film:
        raise HTTPException(status_code=404, detail=f"There is no film with this title - {title}")
    
    return FilmSQLBase.model_validate(film)

@app.get("/films/ai_search/{prompt}/{n_results}")
async def get_film_by_prompt(prompt : Annotated[str, Path(example="Film about space", min_length=3, max_length=150)],
                            n_results: Annotated[int, Path(example=3, ge=1, le=10)],
                            db: Session = Depends(get_sql_db)) -> ChromaQueryFilmsList:
    films = []
    films_list = chroma_service.query(query_text=prompt, n_results=n_results) 
    for film in films_list:
        film_data = (db.query(Film).filter(Film.id==film['id']).first())
        if film_data:
            films.append(FilmSQLBase.model_validate(film_data))

    return ChromaQueryFilmsList(films=films)

