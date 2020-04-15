"""
app/forms.py
ewf215@nyu.edu
10.10.2019
"""

from flask_wtf import FlaskForm		# csrf protection is enabled by default

from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Required
from app.models import User

class RegisterForm(FlaskForm):
	uname = StringField('Username', validators=[DataRequired()])
	pword = PasswordField('Password', validators=[DataRequired()])
	twofa = StringField('2FA Code', validators=[DataRequired()], id='2fa')
	submit = SubmitField('Register')

	def validate_username(self, uname):
		user = User.query.filter_by(username=uname).first()
		if user is not None:
			raise ValidationError('Username taken. Please choose again.')

class LoginForm(FlaskForm):
	uname = StringField('Username', validators=[DataRequired()])
	pword = PasswordField('Password', validators=[DataRequired()])
	twofa = StringField('2FA Code', validators=[DataRequired()], id='2fa')
	submit = SubmitField('Login')

class SpellCheckForm(FlaskForm):
	textfield = TextAreaField('Input Text', render_kw={"rows": 25, "cols": 100})
	submit = SubmitField('Submit')
