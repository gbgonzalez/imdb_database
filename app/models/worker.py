from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float

Base = declarative_base()
class Worker(Base):
    __tablename__ = 'worker'
    cod = Column(String, primary_key=True)
    name = Column(String)
    birth_year = Column(Float)
    death_year = Column(Integer)
    professions = Column(String)