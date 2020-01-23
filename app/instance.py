from flask import Flask
from app.plugins import extensions


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    for extension in extensions:
        extension.init_app(app)

    return app
