from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from pathlib import Path
from flask_migrate import Migrate

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))


db = SQLAlchemy()
migrate = Migrate()

USER_DB='postgres'
PASS_DB='admin'
URL_DB='localhost'
NAME_DB='armeria-america'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'