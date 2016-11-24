# -*- coding: utf-8 -*-
# @Author: paul
# @Date:   2016-11-23 23:06:12
# @Last Modified by:   paul
# @Last Modified time: 2016-11-23 23:13:00
from flask import render_template
from . import app

@app.route('/index')
@app.route('/')
def index():
	user = {'nickname': 'Miguel'}
#     posts = [  # fake array of posts
#     { 
#         'author': {'nickname': 'John'}, 
#         'body': 'Beautiful day in Portland!' 
#     },
#     { 
#         'author': {'nickname': 'Susan'}, 
#         'body': 'The Avengers movie was so cool!' 
#     }
# ]
	return render_template('index.html', title="Python Flask Bucket List App",
		user=user)

if __name__ == "__main__":
	app.run()