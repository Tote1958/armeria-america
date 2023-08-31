from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from app.config.database import db, FULL_URL_DB

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"