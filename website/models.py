#create database models for users and models
from . import db #importing from current packeage(website) the db object
from flask_login import UserMixin
from sqlaclhemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())



class User(db.Model, UserMixin):
    id = db.Column(id.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))