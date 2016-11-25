# -*- coding: utf-8 -*-
# @Author: paul
# @Date:   2016-11-23 23:06:12
# @Last Modified by:   p-chambers
# @Last Modified time: 2016-11-25 12:50:03
from flask import render_template, flash, redirect
from . import app
from .forms import RegistrationForm

@app.route('/index')
@app.route('/')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
    { 
        'author': {'nickname': 'John'}, 
        'body': 'Beautiful day in Portland!' 
    },
    {
        'author': {'nickname': 'Susan'}, 
        'body': 'The Avengers movie was so cool!' 
    }
]
    return render_template('index.html', title="Python Flask Bucket List App",
		                      user=user, posts=posts)

@app.route('/signup', methods=['GET', 'POST'])
def login():
    form = RegistrationForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        flash('Login requested for username={}'.format(
              form.username.data))
        return redirect('/index')
    return render_template('signup.html', 
                           title='Sign In',
                           form=form)


if __name__ == "__main__":
	app.run()