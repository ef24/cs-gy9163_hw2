from flask import flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:/home/pirate/projects/cs_gy9163_hw2/wordflask.db'

db = SQLAlchemy(app)

class ExampleTable(db.Model):
	id = db.Column(db.Integer,primary_key=True)
