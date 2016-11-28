# -*- coding: utf-8 -*-
# @Author: paul
# @Date:   2016-11-23 11:41:39
# @Last Modified by:   p-chambers
# @Last Modified time: 2016-11-28 16:22:32
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


from . import views, models