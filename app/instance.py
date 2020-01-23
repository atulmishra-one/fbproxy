from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from app.plugins import extensions
from app.views import app_views


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    for extension in extensions:
        extension.init_app(app)

    app.register_blueprint(app_views)

    @app.before_first_request
    def re():
        from app import errors

    return app
