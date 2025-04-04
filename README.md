# F.R RestAPI

## Description
This project is a REST API designed to manage a movie database. It provides functionality for handling movie collections, interacting with an SQLite database, and integrating with ChromaDB.

## Project Structure

### Key Files and Directories:
- **`main.py`**: The main entry point for running the API.
- **`database.py`**: Handles interactions with the SQLite database.
- **`models.py`**: Defines the data models used in the application.
- **`schemas.py`**: Contains the data validation schemas.
- **`chromaDB_database_API/`**: Manages ChromaDB integration.
- **`for_chromaDB/`**: Contains utilities for working with ChromaDB.
- **`json_data/`**: Stores JSON files with movie data.

## Features
- CRUD operations for managing movies.
- Integration with ChromaDB for advanced data handling.
- Backup and restore functionality using JSON files.

## How to Run
1. Create and activate a virtual enviroment (optional, but recommended):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate
# on MacOS/Linux
source venv/bin/activate
```

Then, install the required dependencies, use the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

To run the application, execute the folowing comand in terminal.
```
uvicorn main:app --reload
```
Access the API endpoints using your preferred HTTP client (e.g., Postman or cURL).
To view the API documentation, enter the **/docs/** page in application URL.
