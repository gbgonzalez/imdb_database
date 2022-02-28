from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float

Base = declarative_base()
class Movie_worker(Base):
    __tablename__ = 'movie_worker'
    id = Column(Integer, primary_key=True)
    fk_worker = Column(String)
    fk_movie = Column(Float)