"""
app/routes.py
ewf215@nyu.edu
10.10.2019
"""

from app import app
from app.forms import RegisterForm, LoginForm, SpellCheckForm
from app.models import User
from flask import render_template, flash, redirect, url_for, request
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
	# create the registration form
	form = RegisterForm()
	if form.validate_on_submit():
		#add them to the user database
		user = User(username=form.username.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('You are now registered.')
		# ask them to log in
		return redirect(url_for('login'))
	return render_template('register.html', title='Registration Form', form=form)
		
@app.route('/login', methods=['GET', 'POST'])
def login():
	# check if the user is already logged in
	if current_user.is_authenticated:
		return redirect(url_for('spell_check'))
	# create the login form
	form = LoginForm()
	# validate the login attempt
	if form.validate_on_submit():
		# check the database
		user = User.query.filter_by(username=form.username.data).first()
		# if the username is not in the database or if the password is incorrect, redirect back to login page
		if user is not None and user.check_password(form.password.data):
			flash("You have successfully logged in.")
			return redirect(url_for("spell_check"))
		if user is None:
			flash("Invalid username or password.")
		else:
			flash("Invalid username or password.")
	return render_template('login.html', title='Login Form', form=form)

@app.route('/spell_check', methods=['GET', 'POST'])
def spell_check(comments = []):
	form = SpellCheckForm()
	if request.method == 'GET':
		return render_template('spell_check.html', comments=comments)
	#comments.append(request.form['spell_check'])
	return redirect(url_for('spell_check'))
			
	#return render_template('spell_check.html', title='Spell Check Form', form=form)
