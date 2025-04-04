import chromadb
from paths import MAIN_JSON_MOVIES, CHROMADB_PATH

class ChromaDBService:
    def __init__(self):
        self.__session = chromadb.PersistentClient(path=CHROMADB_PATH)
        self.__collection = self.__session.get_collection(name="movies")

    @staticmethod
    def get_metadata_list(results) -> list:
        meta_list = []
        for meta in results["metadatas"][0]:
            meta_list.append(meta)
        return meta_list

    @staticmethod
    def valid_n_results(n_results):
        return 1 <= n_results <= 10

    def query(self, query_text: str, n_results: int = 10) -> list:
        if self.valid_n_results(n_results):
            results = self.__collection.query(
                query_texts=[query_text],
                n_results=n_results,
            )
            return self.get_metadata_list(results)
        else:
            raise ValueError(f"Invalid n_results: {n_results}. Must be between 1 and 50.")