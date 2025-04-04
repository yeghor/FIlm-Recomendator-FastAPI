from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    plot = Column(String)
    release_date = Column(String)
    vote_average = Column(String)

    