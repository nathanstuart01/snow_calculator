from flask import Flask
from instance.config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(DevelopmentConfig)
app.config.from_pyfile('config.py')
db = SQLAlchemy()
db.app = app
db.init_app(app)


from app.routes import base_routes, twenty_four_hour_routes
from app.models import base_data_model, twenty_four_hour_data_model