# -*- coding: utf-8 -*-
# @Author: p-chambers
# @Date:   2016-11-25 15:50:35
# @Last Modified by:   Paul Chambers
# @Last Modified time: 2016-11-30 22:30:05
from . import db, bcrypt
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(160), index=True, unique=True)
    _password = db.Column(db.LargeBinary(120))
    _salt = db.Column(db.String(120))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # authenticated = db.Column(db.Boolean, default=False)

    # def __init__(self, username, password, id, active=True):

    #     self.
    #     self.active = active

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, text_password):
        self._password = bcrypt.generate_password_hash(text_password)

    def check_password(self, text_password):
        return bcrypt.check_password_hash(self._password, text_password)

    def is_authenticated(self):
        return True

    # def authenticate(self):
    #     self.authenticate = True

    def get_id(self):
        return self.email

    def is_anonymous(self):
        # No anonymous user support
        return False
        

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # def __repr__(self):
    #     return '<Post %r>' % (self.body)
