from src import db
from src import app


class Tutor(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    biography = db.Column(db.Text(), nullable=True)
    avaialable = db.Column(db.Boolean(), default=True)
    user = db.relationship('User', back_populates='tutor')