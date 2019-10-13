"""
app/routes.py
ewf215@nyu.edu
10.10.2019
"""

# Per the prof:
# 2FA is optional -- if the user signed up with one, they must use it. 
# If they don't sign up with one, they don't use it. 
# Phone numbers: 10 digits, no spaces, no dashes


from app import app
from app.forms import RegisterForm, LoginForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index.html')
def index():
	return "Hello world!"

@app.route('/register', methods=['GET','POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
			#flash('Login requested for user {}'.format(form.username.data))
			#return redirect('/')
			return 'user {}<br>pass {}<br>2fa {}'.format(
				form.username.data, form.password.data, form.authcode.data)
	return render_template('register.html', title='Registration Form', form=form)
		
@app.route('/login')
def login():
	form = LoginForm()
	if form.validate_on_submit():
			return 'user {}<br>pass {}<br>2fa {}'.format(
				form.username.data, form.password.data, form.authcode.data)
	return render_template('login.html', title='Login Form', form=form)

@app.route('/spell_check')
def spell_check():
	return "Spell check."
	
