from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS


application = Flask(__name__)
application.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(application)
cors = CORS(application, resources={r"/api/*": {"origins": "*"}})
from app.models import *


@application.route('/api/favorites', methods=['GET'])
def api_feature_get():
    favorites_query = Favorites.query.all()
    favorites_list = []
    for i in favorites_query:
        favorites_list.append(i.serialize)
    return jsonify({'favorites': favorites_list}), 200
