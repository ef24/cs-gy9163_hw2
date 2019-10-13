"""
app/forms.py
ewf215@nyu.edu
10.10.2019
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	authcode = StringField('2FA Code', validators=[DataRequired()])
	submit = SubmitField('Register')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	authcode = StringField('2FA Code', validators=[DataRequired()])
	submit = SubmitField('Login')
