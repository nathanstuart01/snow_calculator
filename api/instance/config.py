# This will configure our general settings that we want our differnt environments to have

import os

class Config(object):
	"""Parent Configuration Class """
	DEBUG = False
	SECRET = os.getenv('SECRET')
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
	"""Configuration for development"""
	DEBUG = True
