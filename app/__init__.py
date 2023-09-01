from flask import Flask
from flask_cors import CORS
from app.config.database import *
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    migrate.init_app(app, db)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"
    
    return app



