from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from instance.config import DevelopmentConfig


db = SQLAlchemy()

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(DevelopmentConfig)
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

	return app


