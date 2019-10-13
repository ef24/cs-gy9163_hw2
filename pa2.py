"""
pa2.py
ewf215@nyu.edu
10.10.2019
"""
from app import app, db
from app.models import User

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User}
