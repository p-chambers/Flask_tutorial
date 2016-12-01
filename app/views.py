# -*- coding: utf-8 -*-
# @Author: paul
# @Date:   2016-11-23 23:06:12
# @Last Modified by:   Paul Chambers
# @Last Modified time: 2016-11-30 18:43:14
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required

from . import app, lm, db
from .models import User
from .forms import RegistrationForm

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/index')
@app.route('/')
def index(user=None):
    return render_template('index.html', title="Python Flask Bucket List App",
                           user=user)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        flash('Welcome, {}!'.format(
              form.username.data))
        newuser = User(username=form.username.data, email=form.email.data,
                       password=form.password.data)
        db.session.add(newuser)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', 
                           title='Sign Up (free)',
                           form=form)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if g.user is not None and g.user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['remember_me'] = form.remember_me.data
#         return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
#     return render_template('login.html', 
#                            title='Sign In',
#                            form=form

if __name__ == "__main__":
	app.run()