"""
app/routes.py
ewf215@nyu.edu
01.31.2020
"""

from app import app
from app.forms import RegisterForm, LoginForm, SpellCheckForm
from app.models import User
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from app import db, login
import subprocess
import os

@app.route('/')
def index():
	if current_user.is_authenticated:
		return render_template('index_authenticated.html',
					title = 'Welcome')

	return render_template('index_default.html',
				title = 'Welcome')

@app.route('/register', methods=['GET','POST'])
def register():
	# check if the user is already logged in
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	# create the registration form
	registration_form = RegisterForm()

	if not registration_form.validate_on_submit():
		# render the registration page
		return render_template('register.html', 
					title = 'Registration Form', 
					form = registration_form)

	# parse the user input
	new_username = registration_form.uname.data
	new_password = registration_form.pword.data

	# todo: check if the user exists already
	user = User.query.filter_by(username = new_username).first()

	if user is not None:
		flash('Failure. The user already exists.')
		return redirect(url_for('register'))

	# otherwise, add a new user to the database
	else:
		new_user = User(username = new_username)
		new_user.set_password(new_password)
		db.session.add(new_user)
		db.session.commit()

		flash('Way to go! Your registration was a success.')

		# send the new user to the login page
		return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

	# check if the user is already logged in
	if current_user.is_authenticated:
		return redirect(url_for('index'))

	# create the login form
	login_form = LoginForm()

	if not login_form.validate_on_submit():
		# render the login page
		return render_template('login.html',
				       	title = 'Login Form',
					form = login_form)

	# parse the user input
	the_username = login_form.uname.data
	the_password = login_form.pword.data
	the_authcode = login_form.authcode.data

	# validate the username
	user = User.query.filter_by(username = the_username).first()

	if user is not None and user.check_password(the_password):
		# the username and the password are good
		# todo: what about the authcode?
		login_user(user)
		return redirect(url_for('index'))

	flash('Incorrect! Something isn\'t quite right. Try again.')
	return redirect(url_for('login'))

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/spell_check', methods=['GET', 'POST'])
def spell_check(comments = []):

	# check if the user is already logged in
	if not current_user.is_authenticated:
		return redirect(url_for('login'))

	# create the spell check form
	spell_check_form = SpellCheckForm()

	if not spell_check_form.validate_on_submit():
		# render the spell check page
		return render_template('spell_check.html',
				       	title = 'Spell Check Request',
					form = spell_check_form)

	# parse the user input
	text_to_check = spell_check_form.textfield.data

	# create the file, run the spell check request, capture the output, and delete the file
	the_file = open("/tmp/text", "w")
	the_file.write(text_to_check)
	the_file.close()
	spell_check_output = subprocess.check_output(['/home/elisabeth/cs-gy9163/cs-gy9163_hw1/bin/spell', '/tmp/text', '/home/elisabeth/cs-gy9163/cs-gy9163_hw1/wordlist.txt'], universal_newlines=True)
	
	if not spell_check_output:
		flash("I didn't find any spelling errors!")
		
	os.remove("/tmp/text")
	
	#todo: parse the result from subprocess.check_output
	#todo: what is the command we need to run? arguments?
	
	return render_template('spell_check.html', 
				title = 'Spell Check Result',
				form = spell_check_form,
				result = spell_check_output)
