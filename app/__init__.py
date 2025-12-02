from flask import Flask
from .config import Config
from .db import mongo

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)   # MongoDB init

    from .routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
