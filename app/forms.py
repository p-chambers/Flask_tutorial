# -*- coding: utf-8 -*-
# @Author: p-chambers
# @Date:   2016-11-24 16:24:27
# @Last Modified by:   p-chambers
# @Last Modified time: 2016-12-01 13:40:55
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, PasswordField,\
    SubmitField


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField('Email Address', validators=[
        validators.Length(min=6, max=35),
        validators.Email("please enter a valid email address")])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[
        validators.Length(min=6, max=35),
        validators.Email("please enter a valid email address")
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
    ])
    remember_me = BooleanField('Remember me', default=False)
    submit = SubmitField("Sign in")
