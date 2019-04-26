from flask import Flask
from flask_cors import CORS
from instance.config import ProductionConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(ProductionConfig)
app.config.from_pyfile('config.py')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
db = SQLAlchemy()
db.app = app
db.init_app(app)


from app.routes import base_routes, twenty_four_hour_routes
from app.models import base_data_model, twenty_four_hour_data_model
