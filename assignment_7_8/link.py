from typing import List
from flask_restful import Resource
import csv


class Link():

    def __init__(self, movieId: int, imdbdId: int, tmdbId: int):
        self.id = movieId
        self.imdbId = imdbdId
        self.tmdbId = tmdbId

    def __str__(self) -> str:
        return f"""Link {self.id},
 with imdbId: {self.imdbId} and tmdbId: {self.tmdbId}"""


class Links(Resource):

    links: List[Link] = []

    def __init__(self) -> None:
        super().__init__()
        with open("links.csv", newline='') as link_file:
            link_rows = csv.reader(link_file, delimiter=",")
            for row in link_rows:
                self.links.append(Link(row[0], row[1], row[2]))

    def get(self):
        return [link.__dict__ for link in self.links]
