import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

"""
From PyBites Bite 30: https://codechalleng.es/bites/30/
"""

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = defaultdict(list)
    with open(MOVIE_DATA, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                director = row.get('director_name')
                title_year = int(row['title_year'])
                if title_year < MIN_YEAR:
                    continue
                movie = Movie(title=row['movie_title'].rstrip(),
                              year=title_year,
                              score=float(row['imdb_score']))
                movies[director].append(movie)
            except ValueError:
                continue
        return movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    scores = [movie.score for movie in movies]
    return round(sum(scores) / len(scores), 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    scores = []
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            avg_score = calc_mean_score(movies)
            scores.append((director, avg_score))
    return sorted(scores, key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    directors = get_movies_by_director()
    scores = get_average_scores(directors)
    print(scores[:10])
