from datetime import datetime, time, timedelta
from typing import List
from flask_restful import Resource
import csv


class Rating():

    def __init__(self, userId: int, movieId: int, rating: int,
                 timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = datetime.fromtimestamp(
            int(timestamp)
        )

    def __str__(self) -> str:
        return f"""Rating by user: {self.userId},
 for movie: {self.movieId}, rate: {self.rating},
 on: {self.timestamp}"""


class Ratings(Resource):

    ratings: List[Rating] = []

    def __init__(self) -> None:
        super().__init__()
        with open("ratings.csv", newline='') as rating_file:
            rating_rows = csv.reader(rating_file, delimiter=",")
            for row in rating_rows:
                self.ratings.append(Rating(row[0], row[1], row[2], row[3]))

    def get(self):
        return [rating.__dict__ for rating in self.ratings]
