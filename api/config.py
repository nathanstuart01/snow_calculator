import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

	SQLALCHEMY_DATABASE_URI = os.environ.get('POSTGRES_URL')
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

