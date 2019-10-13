"""
config.py
ewf215@nyu.edu
10.10.2019
"""
import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'sasha'
