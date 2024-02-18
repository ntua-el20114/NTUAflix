from flask import Flask
from .routes.Catalogue import catalogue
from .routes.LogIn import login
from .routes.MovieProfile import movie_profile
from .routes.PersonProfile import person_profile
from .routes.SearchResults import search_results
from .routes.UserProfile import user_profile
from .routes.Welcome import welcome
from .routes.ByGenre import bygenre


def create_app():
    app = Flask(__name__)
    app.register_blueprint(catalogue)
    app.register_blueprint(login)
    app.register_blueprint(movie_profile)
    app.register_blueprint(person_profile)
    app.register_blueprint(search_results)
    app.register_blueprint(user_profile)
    app.register_blueprint(welcome)
    app.register_blueprint(bygenre)
    return app