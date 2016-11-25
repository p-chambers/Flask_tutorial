# -*- coding: utf-8 -*-
# @Author: p-chambers
# @Date:   2016-11-25 15:50:35
# @Last Modified by:   p-chambers
# @Last Modified time: 2016-11-25 16:21:47
from . import db
from flask.ext.login import UserMixin
from flask.ext.sqlalchemy.ext.hybrid import hybrid_property

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(160), index=True, unique=True)
    _password = db.Column(db.LargeBinary(120))
    _salt = db.Column(db.String(120))

    @hybrid_property
    def password():
        pass

    def __repr__(self):
