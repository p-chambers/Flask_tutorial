# -*- coding: utf-8 -*-
# @Author: p-chambers
# @Date:   2016-11-24 16:24:27
# @Last Modified by:   p-chambers
# @Last Modified time: 2016-11-25 12:48:57
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, PasswordField, StringField, BooleanField


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


# class LoginForm(Form):
