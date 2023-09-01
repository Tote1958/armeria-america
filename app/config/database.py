from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))



db = SQLAlchemy()
USER_DB='postgres'
PASS_DB='admin'
URL_DB='localhost'
NAME_DB='armeria-america'

FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'