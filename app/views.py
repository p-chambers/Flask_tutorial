# -*- coding: utf-8 -*-
# @Author: paul
# @Date:   2016-11-23 23:06:12
# @Last Modified by:   Paul Chambers
# @Last Modified time: 2016-12-02 14:33:06
from flask import render_template, flash, redirect, session, url_for, request,\
   g, abort
from flask_login import login_user, logout_user, current_user, login_required

from six.moves.urllib.parse import urlparse, urljoin

from . import app, lm, db
from .models import User
from .forms import RegistrationForm, LoginForm

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user


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
                           title='Sign Up',
                           form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(form.password.data):
          print('id = '.format(session.get("user_id")))
          if login_user(user, remember=form.remember_me.data):
              flash("Logged in!")
              next = request.args.get('next')
              if not is_safe_url(next):
                  return abort(400)
              return redirect(next or url_for("index"))
          else:
              flash("Sorry, but you could not log in.")
        else:
          return redirect(url_for('login'))

    return render_template('login.html', 
                           title='Log In',
                           form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("Logged out successfully")
    return redirect(url_for('index'))

if __name__ == "__main__":
	app.run()