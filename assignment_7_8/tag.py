from datetime import datetime, timedelta
from typing import List
from flask_restful import Resource
import csv


class Tag():

    def __init__(self, userId: int, movieId: int, tag: str,
                 timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f"""Tag by user: {self.userId},
 for movie: {self.movieId}, tag: {self.rating},
 on: {self.timestamp}"""


class Tags(Resource):

    tags: List[Tag] = []

    def __init__(self) -> None:
        super().__init__()
        with open("assingment_7_8/tags.csv", newline='') as tag_file:
            tags_row = csv.reader(tag_file, delimiter=",")
            for row in tags_row:
                self.tags.append(Tag(row[0], row[1], row[2], row[3]))

    def get(self):
        return [tag.__dict__ for tag in self.tags]
