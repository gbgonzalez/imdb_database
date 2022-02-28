from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
import os

def database_connect(target: str = "colorectal"):
    if target == "imdb":
        engine = create_engine(
            #"mysql+pymysql://tweetUser:tweetPass@192.168.200.134:3306/tweet_corona?charset=utf8mb4"
            "mysql+pymysql://imdbUser:imdbPass@localhost:3306/imdb?charset=utf8mb4"
        )
    Session = sessionmaker(bind=engine)

    return Session()