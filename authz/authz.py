from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from authz.config import Config

db = SQLAlchemy()

apiv1_bp = Blueprint("apiv1", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

from authz import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load from environment variables.
    db.init_app(app)  # Initialize SQLALCHEMY database object.
    app.register_blueprint(apiv1_bp)
    return app