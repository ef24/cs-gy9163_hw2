"""
app/__init__py
ewf215@nyu.edu
10.10.2019
"""
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# import package modules
from app import routes
