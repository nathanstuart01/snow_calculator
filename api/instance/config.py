# This will configure our general settings that we want our differnt environments to have

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	"""Parent Configuration Class """
	DEBUG = False
	SECRET = os.getenv('SECRET')
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
	"""Configuration for development"""
	DEBUG = True

