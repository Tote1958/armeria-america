from flask import Flask
from flask_migrate import Migrate
from app.config import *
from models.User import User

app = Flask(__name__)


db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"