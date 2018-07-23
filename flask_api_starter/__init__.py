from flask import Flask
from flask_api_starter.config import Config


def create_app(app_name):
    app = Flask(app_name)

    app.config.from_object(Config)

    from flask_api_starter.apiv1 import apiv1
    app.register_blueprint(apiv1, url_prefix='/api/v1')

    return app
