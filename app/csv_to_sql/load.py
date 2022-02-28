from models import Movie, Rating, Movie_worker, Worker

def csv_to_movie(csv):

    if csv[5] == "\\N":
        year = None
    else:
        year = int(csv[5])

    if csv[8] == "\\N":
        genres = None
    else:
        genres = csv[8]

    return Movie(
        cod=csv[0],
        title = csv[2],
        year = year,
        genres = genres)

def csv_to_rating(csv):
    return Rating(
        movie_cod = csv[0],
        avg_rating = float(csv[1]),
        num_votes = int(csv[2])
    )

def csv_to_workers(csv, session):
    movie_workers = []

    if csv[2] == "\\N":
        birthYear = None
    else:
        birthYear = int(csv[2])

    if csv[3] == "\\N":
        deathYear = None
    else:
        deathYear = int(csv[3])
    worker = Worker(
        cod=csv[0],
        name = csv[1],
        birth_year = birthYear,
        death_year = deathYear,
        professions = csv[4]
        )
    return worker


def csv_to_worker_movies(csv, session):
    worker_movies = []
    for cod_movie in csv[5].split(","):
        # SELECT * FROM movie WHERE id = cod_movie
        movie = session.query(Movie).get(cod_movie)
        if movie:
            worker_movie = Movie_worker(
                fk_worker=csv[0],
                fk_movie = cod_movie
            )
            worker_movies.append(worker_movie)
    return worker_movies

