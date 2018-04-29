from app import app 
from app import db
import psycopg2

class UtahSkiAreas(db.Model):
	"""This class represents the Utah ski areas information table """
	""" Eventually add in vertical info, acreage info, annual snowfall, standard deviation snowfall, historical snowfall, ticket prices, average lift time, self calcualted overall rating ??"""

	__tablename__='areas'

	area_id = db.Column(db.Integer, primary_key=True, nullable=False)
	area_name = db.Column(db.String(255), nullable=False)

	def __repr__(self):
		return '<UtahSkiAreas %r>' % self.area_name