# -*- coding: utf-8 -*-
# @Author: p-chambers
# @Date:   2016-11-25 15:50:35
# @Last Modified by:   p-chambers
# @Last Modified time: 2016-11-28 18:03:03
from . import db
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, \
     check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(160), index=True, unique=True)
    _password = db.Column(db.LargeBinary(120))
    _salt = db.Column(db.String(120))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @hybrid_property
    def password():
        pass

    # def is_authenticated(self):

    # def is_active(self):

    # def is_anonymous(self):

    # def get_id(self):
        
    # def __repr__(self):
    #     return '<User %r>' % (self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # def __repr__(self):
    #     return '<Post %r>' % (self.body)
