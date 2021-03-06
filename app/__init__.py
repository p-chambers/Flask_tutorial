# -*- coding: utf-8 -*-
# @Author: paul
# @Date:   2016-11-23 11:41:39
# @Last Modified by:   Paul Chambers
# @Last Modified time: 2016-12-02 12:32:57
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object('config')

bcrypt = Bcrypt(app)

db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


from . import views, models