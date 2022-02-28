import argparse
import csv
from csv_to_sql import csv_to_movie, csv_to_rating, csv_to_workers, csv_to_worker_movies
from pathlib import Path
from db.connect import database_connect
from models import Movie, Worker


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--option", type=str, help="select an option of BERT machine learning")
    args = parser.parse_args()
    path = Path.cwd()
    session = database_connect("imdb")


    if args.option == "insert_movies":
        #python app\imdb_scripts.py -o insert_movies
        csv_route = f"{str(path)}/files/titles.csv"

        with open(csv_route, 'r', encoding="UTF8") as csv_file:
            rows = csv.reader(csv_file, delimiter="\t")
            for i, row in enumerate(rows):

                if i != 0:
                    if row[1] == "movie" and row[4] == "0":
                        movie = csv_to_movie(row)
                        # INSERT INTO movie VALUES....
                        session.add(movie)

                    if i % 1000 == 0 and i != 0:
                        try:
                            print(i)
                            session.commit()
                        except Exception as e:
                            print(f"Exception {e}")
                            pass

    if args.option == "insert_rating":
        # python app\imdb_scripts.py -o insert_rating
        csv_route = f"{str(path)}/files/ratings.tsv"

        with open(csv_route, 'r', encoding="UTF8") as csv_file:
            rows = csv.reader(csv_file, delimiter="\t")
            for i, row in enumerate(rows):
                if i != 0:
                    #SELECT * FROM movie WHERE cod = row[0]
                    movie = session.query(Movie).get(row[0])
                    # adds rating only if movie exist
                    if movie:
                        rating = csv_to_rating(row)
                        # INSERT INTO rating VALUES....
                        session.add(rating)

                if i % 1000 == 0 and i != 0:
                    try:
                        print(i)
                        session.commit()
                    except Exception as e:
                        print(f"Exception {e}")
                        pass

    if args.option == "insert_workers":
        # python app\imdb_scripts.py -o insert_workers
        csv_route = f"{str(path)}/files/workers.tsv"
        with open(csv_route, 'r', encoding="UTF8") as csv_file:
            rows = csv.reader(csv_file, delimiter="\t")
            for i, row in enumerate(rows):
                if i != 0:
                    cod_movies = row[5].split(",")
                    exist_movie = False
                    for cod_movie in cod_movies:
                        # SELECT * FROM movie WHERE cod = cod_movie
                        movie = session.query(Movie).get(cod_movie)
                        # adds worker only if movie exist
                        if movie:
                            exist_movie = True

                    if exist_movie:
                        worker = csv_to_workers(row, session)
                        # INSERT INTO worker VALUES....
                        session.add(worker)

                if i % 1000 == 0 and i != 0:
                    try:
                        print(i)
                        session.commit()
                    except Exception as e:
                        print(f"Exception {e}")
                        pass

    if args.option == "insert_movie_workers":
        # python app\imdb_scripts.py -o insert_movie_workers
        csv_route = f"{str(path)}/files/workers.tsv"
        with open(csv_route, 'r', encoding="UTF8") as csv_file:
            rows = csv.reader(csv_file, delimiter="\t")
            for i, row in enumerate(rows):
                if i != 0:
                    worker = session.query(Worker).get(row[0])
                    if worker:
                        worker_movies = csv_to_worker_movies(row, session)
                        for worker_movie in worker_movies:
                            # INSERT INTO movie VALUES....
                            session.add(worker_movie)
                if i % 1000 == 0 and i != 0:
                    try:
                        print(i)
                        session.commit()
                    except Exception as e:
                        print(f"Exception {e}")
                        pass
