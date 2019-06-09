from app import db
from sqlalchemy import DateTime
import datetime
from sqlalchemy.sql import func


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

