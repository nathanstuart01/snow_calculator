from app import app
from app import db

class UtahBaseTotals(db.Model):
	"""This class represents the base totals table """

	__tablename__='base_totals'

	id = db.Column(db.Integer, primary_key=True, nullable=False)
	area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=False)
	area_name = db.Column(db.String(255), nullable=False)
	base_total = db.Column(db.Integer, nullable=False)
	crawled_at = db.Column(db.DateTime, nullable=False)

	def __repr__(self):
		return '<UtahBaseTotals (%r, %r, %r, %r)>' % (self.area_id, self.area_name, self.base_total, self.crawled_at)
