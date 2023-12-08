from .database import db

import datetime

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    users = db.relationship('User', backref='role', cascade  = 'all,delete-orphan')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, default=1)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, default=2)
    albums = db.relationship('Album', backref='user', cascade ='all,delete-orphan')

class Album(db.Model):
    __tablename__ = 'album'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    artist = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    songs = db.relationship('Song', backref='album', cascade ='all,delete-orphan')


class Song(db.Model):
    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    lyrics = db.Column(db.String)
    duration = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    



    
