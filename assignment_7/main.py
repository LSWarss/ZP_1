from movie import Movies
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(Movies, "/")

if __name__ == '__main__':
    app.run(debug=True)
