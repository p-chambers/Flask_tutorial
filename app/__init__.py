# -*- coding: utf-8 -*-
# @Author: paul
# @Date:   2016-11-23 11:41:39
# @Last Modified by:   paul
# @Last Modified time: 2016-11-23 23:14:18
from flask import Flask, render_template

app = Flask(__name__)

from . import views