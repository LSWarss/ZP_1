
from movie import Movies
from link import Links
from flask import Flask
from rating import Ratings
from tag import Tags
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(Movies, "/movies")
api.add_resource(Links, "/links")
api.add_resource(Ratings, "/ratings")
api.add_resource(Tags, "/tags")

if __name__ == '__main__':
    app.run(debug=True)
