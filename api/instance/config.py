# This will configure our general settings that we want our differnt environments to have
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
	"""Parent Configuration Class """
	DEBUG = False
	SECRET = os.getenv('SECRET')
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	


class ProductionConfig(Config):
	"""Configuration for development"""
	DEBUG = False



