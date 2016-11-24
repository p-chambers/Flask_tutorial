# -*- coding: utf-8 -*-
# @Author: paul
# @Date:   2016-11-23 11:41:39
# @Last Modified by:   p-chambers
# @Last Modified time: 2016-11-24 16:21:57
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

from . import views