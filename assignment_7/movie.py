from typing import List
from flask_restful import Resource
import csv


class Movie():

    def __init__(self, movieId: int, title: str, genres: List[str]):
        self._movieId = movieId
        self._title = title
        self._genres = genres

    def __str__(self) -> str:
        return f"Movie {self._movieId}: {self._title}, genres: {self._genres}"


class Movies(Resource):

    movies: List[str] = []

    def __init__(self) -> None:
        super().__init__()
        with open("movies.csv", newline='') as movies_file:
            moviesRows = csv.reader(movies_file, delimiter=",")
            for row in moviesRows:
                self.movies.append(Movie(row[0], row[1], row[2].split("|")))

    def get(self):
        return [movie.__dict__ for movie in self.movies]