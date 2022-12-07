from config import db, app
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50), unique=True)
    phone_number = db.Column(db.Integer, unique=True)
    date_joined = db.Column(db.Date, default=datetime.utcnow())


with app.app_context():
    db.create_all()