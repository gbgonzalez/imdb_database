from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean

Base = declarative_base()
class Movie(Base):
    __tablename__ = 'movie'
    cod = Column(String, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    genres = Column(String)