from app import db
from sqlalchemy import DateTime
import datetime
from sqlalchemy.sql import func
from sqlalchemy_utils import ChoiceType


class Field(db.Model):
    TYPES = [
        ('text', 'number', 'date', 'enum')
    ]
    __tablename__ = 'flield'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(ChoiceType(TYPES))


class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(10))
    ranking = db.Column(db.Integer, nullable=False)
    created_date = db.Column(DateTime, default=datetime.datetime.utcnow)
    category_area_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='favorites')
    last_time = db.Column(DateTime, onupdate=func.utc_timestamp())

    def __init__(self, title, description, ranking, created_date, category_area_id):
        self.title = title
        self.description = description
        self.ranking = ranking
        self.created_date = created_date
        self.category_area_id = category_area_id
    @property
    def serialize(self):
        """
        Return serialized feature info
        :return dict:
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'ranking': self.ranking,
            'created_date': self.created_date,
        }


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, title):
        self.title = title

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }







