import flask
import flask_restful

from . import routes


def create_app():
    app = flask.Flask(__name__)
    create_api(app)
    return app


def create_api(app):
    api = flask_restful.Api(app)
    routes.add_resources(api)
    return api
