import random

from imdb import IMDb, IMDbDataAccessError


def get_movie():

    ia = IMDb()

    try:
        movie_id = str(random.randint(300, 2794046)).zfill(8)
        print(movie_id)
        movie = ia.get_movie(movie_id)
    except IMDbDataAccessError:
        pass
    finally:
        return movie


# ia = IMDb()
# movie = ia.get_movie(random.randint(300, 2794046))
movie = get_movie()
print(movie.keys())