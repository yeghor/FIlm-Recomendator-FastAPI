import os

SQL_DB_PATH = 'sqlite:///database.db'
MAIN_JSON_MOVIES = os.path.join(os.path.dirname(__file__), "json_data", "films_data_w_keywords.json")
CHROMADB_PATH = os.path.join(os.path.dirname(__file__), "chromaDB_database_API")

print(MAIN_JSON_MOVIES)
print(CHROMADB_PATH)