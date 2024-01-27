from src import db
from enum import Enum
from src import app

class User(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), nullable=False , unique=True)
    phone_number = db.Column(db.String(20), nullable=True , unique=True)
    birthdate = db.Column(db.Date(), nullable=True)
    password = db.Column(db.String(256), nullable=False)
    university = db.Column(db.String(100), nullable=True)
    gender = db.Column(db.String(6), nullable=True)
    profile_picture_blob = db.Column(db.LargeBinary(), nullable=True)  # Store the image directly in the database
    online = db.Column(db.Boolean(), default=False)
    active = db.Column(db.Boolean(), default=False)
    last_time_online = db.Column(db.DateTime(), nullable=True)
    role = db.Column(db.String(10), nullable=False)
    tutor = db.relationship('Tutor', back_populates='user', uselist=False, cascade='all, delete-orphan')
    learner = db.relationship('Learner', back_populates='user', uselist=False, cascade='all, delete-orphan')