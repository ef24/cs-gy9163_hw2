"""
app/__init__py
ewf215@nyu.edu
04.07.2020
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

# import package modules
from app import routes, models

# jinja configuration
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True