from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float

Base = declarative_base()
class Rating(Base):
    __tablename__ = 'rating'
    id = Column(Integer, primary_key=True)
    movie_cod = Column(String)
    avg_rating = Column(Float)
    num_votes = Column(Integer)