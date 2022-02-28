from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
import os

def database_connect(target):
    if target == "imdb":
        engine = create_engine(
            "mysql+pymysql://imdbUser:imdbPass@localhost:3306/imdb?charset=utf8mb4"
        )
    Session = sessionmaker(bind=engine)

    return Session()