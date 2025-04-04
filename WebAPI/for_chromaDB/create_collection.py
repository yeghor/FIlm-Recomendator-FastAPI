from paths import MAIN_JSON_MOVIES, CHROMADB_PATH
import json
import chromadb

client = chromadb.PersistentClient(path=CHROMADB_PATH)
collection = client.create_collection(name="movies")

with open(MAIN_JSON_MOVIES, "r") as file:
    movies = json.load(file)

docs = []
metadatas = []
ids = []

for index, movie in enumerate(movies):
    movie_embeding = str(movie["original_title"]) + " " + str(movie["overview"]) + " " + str(movie["release_date"] + " " + str(movie["key_words"]))
    movie_meta = {
        "id": movie["id"]
    }
    docs.append(movie_embeding)
    metadatas.append(movie_meta)
    ids.append("id" + str(index))

collection.add(
    documents=docs,
    metadatas=metadatas,
    ids=ids
)    