from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from paths import SQL_DB_PATH

engine = create_engine(SQL_DB_PATH, connect_args={"check_same_thread": False})
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()