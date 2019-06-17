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
def api_favorite_get():
    favorites_query = Favorites.query.all()
    favorites_list = []
    for i in favorites_query:
        favorites_list.append(i.serialize)
    return jsonify({'favorites': favorites_list}), 200

# Retrieve single favorite on api/favorites/<id>
@application.route('/api/favorites/<int:id>', methods=['GET'])
def api_single_favorite_get(id):
    favorite = Favorites.query.get(id)
    return jsonify({'favorite': favorite.serialize}), 201


# Delete single favorite on api/favorites/<id>
@application.route('/api/favorites/<int:id>', methods=['DELETE'])
def api_favorite_delete(id):
    favorite = Favorites.query.get(id)
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({'message': 'Favorite deleted successfully'}), 201


# Create new favorite
@application.route('/api/favorites', methods=['POST'])
def api_favorite_post():
    ranking = request.json.get('ranking') \
        if request.json.get('ranking') \
        else db.session.query(db.func.max(Favorites.ranking)).filter(Favorites.category == request.json.get('selected')).scalar() + 1 or 1

    favorites = Favorites.query.filter(Favorites.category_area_id == request.json.get('selected'), Favorites.ranking >= ranking).order_by(Favorites.ranking).all()
    i = int(ranking)

    for favorite in favorites:
        favorite.ranking = i + 1
        i += 1
        db.session.commit()
    created_date = datetime.datetime.strptime(request.json.get('created_date'), '%m-%d-%Y')
    data = Favorites(request.json.get('title'),
                     request.json.get('description'),
                     ranking,
                     created_date,
                     request.json.get('selected'),
                     )

    db.session.add(data)
    db.session.commit()
    return jsonify({'favorite': data.serialize}), 201


# Edit single favorite on api/favorites/<id>
@application.route('/api/favorites/<int:id>', methods=['PUT'])
def api_favorite_put(id):
    ranking = request.json.get('ranking') if request.json.get('ranking') else db.session.query(db.func.max(Favorites.ranking)).filter(Favorites.category_area_id ==request.json.get('selected')).scalar() + 1 or 1
    favorites = Favorites.query.filter(Favorites.category_area_id == request.json.get('selected'), Favorites.ranking >= ranking).order_by(Favorites.ranking).all()
    i = int(ranking)
    for favorite in favorites:
        favorite.ranking = i + 1
        i += 1
        db.session.commit()
    favorite = Favorites.query.get(id)
    favorite.title = request.json.get('title')
    favorite.description = request.json.get('description')
    favorite.ranking = ranking
    favorite.category_area_id = request.json.get('selected')
    db.session.commit()

    return jsonify({'message': 'Favorite edited successfully'}), 201



# Categories GET API
@application.route('/api/categories/', methods=['GET'])
def api_client_get():
    category_query = Category.query.all()
    category_list = []
    for c in category_query:
        category_list.append(c.serialize)
    return jsonify({'categories': category_list})

