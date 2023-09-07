from flask import Flask
from flask_cors import CORS
from app.config.database import *
from flask_migrate import Migrate
from app.models import *

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    migrate.init_app(app, db)

    from app.resources import home, client  
    app.register_blueprint(home, url_prefix='/api/v1')
    app.register_blueprint(client, url_prefix='/api/v1')


    
    return app



