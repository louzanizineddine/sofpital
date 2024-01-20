from src import db
from src import app


class Learner(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='learner')