from collections import Counter, namedtuple, defaultdict
import csv
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))
# Change the current working directory to the script's location
os.chdir(script_dir)

movies_csv = "movies_csv.csv"
Movie = namedtuple("Movie", "title year score")


def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors

directors = get_movies_by_director()
# print(directors["Christopher Nolan"])

cnt = Counter()
for director, movies in directors.items():
    cnt[director] += len(movies)
    
print(cnt.most_common(5))