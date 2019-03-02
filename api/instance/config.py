# This will configure our general settings that we want our differnt environments to have
from flask_sqlalchemy import SQLAlchemy
import os

class Config(object):
	"""Parent Configuration Class """
	DEBUG = False
	SECRET = os.getenv('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	


class ProductionConfig(Config):
	"""Configuration for development"""
	DEBUG = False



