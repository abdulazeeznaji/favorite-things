from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS
from datetime import datetime


application = Flask(__name__)
application.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(application)
cors = CORS(application, resources={r"/api/*": {"origins": "*"}})
from app.models import *


# Fetch all favorites
@application.route('/api/favorites', methods=['GET'])
def api_feature_get():
    favorites_query = Favorites.query.all()
    favorites_list = []
    for i in favorites_query:
        favorites_list.append(i.serialize)
    return jsonify({'favorites': favorites_list}), 200


# Create new favorite
@application.route('/api/favorites', methods=['POST'])
def api_favorite_post():

    ranking = request.json.get('ranking') \
        if request.json.get('ranking') \
        else db.session.query(db.func.max(Favorites.ranking)).filter(Favorites.category == request.json.get('category')).scalar() + 1 or 1

    favorites = Favorites.query.filter(Favorites.category_area_id == request.json.get('category'), Favorites.ranking >= ranking).order_by(Favorites.ranking).all()
    i = int(ranking)

    for favorite in favorites:
        favorite.ranking = i + 1
        i += 1
        db.session.commit()
    created_date = datetime.datetime.strptime(request.json.get('created_date'), '%d-%m-%Y')
    data = Favorites(request.json.get('title'),
                     request.json.get('description'),
                     ranking,
                     created_date,
                     request.json.get('category'),
                     )

    db.session.add(data)
    db.session.commit()
    return jsonify({'message': 'Favorite successfully added'}), 201