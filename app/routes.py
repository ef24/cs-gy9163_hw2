"""
app/routes.py
ewf215@nyu.edu
10.10.2019
"""

from app import app
from app.forms import RegisterForm, LoginForm
from app.models import User
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from app import db, login
 

@app.route('/')
@app.route('/index.html')
def index():
	return "Hello world!"

@app.route('/register', methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(username=form.username.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('You are now registered.')
		return redirect(url_for('login'))
			#flash('Login requested for user {}'.format(form.username.data))
			#return redirect('/')
		#return 'user {}<br>pass {}<br>2fa {}'.format(
			#form.username.data, form.password.data, form.authcode.data)
	return render_template('register.html', title='Registration Form', form=form)
		
@app.route('/login', methods=['GET', 'POST'])
def login():
	# check if the user is already logged in
	if current_user.is_authenticated:
		return redirect(url_for('index'))
		
	# create the login form
	form = LoginForm()
	
	# validate the login attempt
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			return redirect(url_for('login'))
		#login_user(user, remember=form.remember_me.data)
		return redirect(url_for('index'))
			#return 'user {}<br>pass {}<br>2fa {}'.format(
				#form.username.data, form.password.data, form.authcode.data)
	return render_template('login.html', title='Login Form', form=form,)

@app.route('/spell_check')
def spell_check():
	return "Spell check."

#TO DO:
# Check if username is in database
# If not in database, then register & create register
# Then send to login page
# Go through registration process, go through pseudocode, translate to code
# Write it out in words exactly what's going on in the process
# Think about what's going on with the spellcheck and what we'll do there
# E.g., Get something from the user to check, tell user whether it's valid or not, etc.
# Monday/Tues testing of registration/login
