from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Annotated

class FilmBase(BaseModel):
    title: str

class FilmSQLBase(FilmBase):
    plot: str
    release_date: str
    id: int
    vote_average: str

    class Config:
        from_attributes = True


class AllFilmsWithPagination(BaseModel):
    page: Annotated[int, Field(ge=1, le=40, title="Number of page. 1 page = 10 results")]

class AllFilms(BaseModel):
    films: List[FilmSQLBase]

class ChromaQuery(BaseModel):
    query_text: Annotated[str, Field(title="String that must contain details of film")]
    n_results: Annotated[int, Field(ge=1, le=10, title="For how many films results will be searched")]

class ChromaQueryFilmsList(AllFilms):
    pass
