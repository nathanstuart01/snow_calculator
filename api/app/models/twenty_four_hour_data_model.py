from app import app 
from app import db
import psycopg2

class UtahTwentyFourHourTotals(db.Model):
	"""This class represents the twenty four hour totals table """

	__tablename__='twenty_four_hour_totals'

	id = db.Column(db.Integer, primary_key=True, nullable=False)
	area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=False)
	area_name = db.Column(db.String(255), nullable=False)
	twenty_four_hour_total = db.Column(db.Integer, nullable=False)
	crawled_at = db.Column(db.DateTime, nullable=False)

	def __repr__(self):
		return '<UtahTwentyFourHourTotals (%r, %r, %r)>' % (self.area_name, self.twenty_four_hour_total, self.crawled_at)