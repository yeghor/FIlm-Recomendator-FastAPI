from database import engine, session_local
from models import Film, Base
from paths import MAIN_JSON_MOVIES
import json

db = session_local()
Base.metadata.create_all(bind=engine)

with open(MAIN_JSON_MOVIES, 'r') as file:
    films = json.load(file)
    print(films)
    

db.query(Film).delete()
db.commit()
for film in films:
    existing_film = db.query(Film).filter_by(id=film["id"]).first()
    if not existing_film:
        db_film = Film(id=film['id'], title=film["title"], plot=film["overview"], release_date=film["release_date"], vote_average=film["vote_average"])
        db.add(db_film)
        db.commit()
        db.refresh(db_film)
        print(f"Film id = {film["id"]}, title = {film["title"]} added succesfuly")
    else:
        print(f"Film {film["title"]} allready exists. Skipping.")

