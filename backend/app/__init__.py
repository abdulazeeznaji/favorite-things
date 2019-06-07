from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

application = Flask(__name__)
application.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(application)