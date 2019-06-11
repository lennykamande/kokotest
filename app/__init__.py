# api/__init__.py
import flask
from flask_api import FlaskAPI

# local import
from instance.config import app_config

# initialize sql-alchemy in case of any database


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    from .api.V1 import version1 as v1
    app.register_blueprint(v1)

    from .api.V2 import version2 as v2
    app.register_blueprint(v2)
    
    return app