"""
app/forms.py
ewf215@nyu.edu
10.10.2019
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Required
from app.models import User


class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
	authcode = StringField('2FA Code', validators=[DataRequired()])
	submit = SubmitField('Register')
	
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Username taken. Please choose again.')

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	authcode = StringField('2FA Code', validators=[DataRequired()])
	submit = SubmitField('Login')
