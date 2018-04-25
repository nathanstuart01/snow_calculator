from app import db
import psycopg2

class UtahSkiAreas(db.Model):
	"""This class represents the Utah ski areas information table """

	__tablename__='areas'

	area_id = db.Column(db.Integer, primary_key=True, nullable=False)
	area_name = db.Column(db.String(255), nullable=False)

	def __repr__(self):
		return '<UtahSkiAreas %r>' % self.area_name



class UtahBaseTotals(db.Model):
	"""This class represents the base totals table """

	__tablename__='base_totals'

	id = db.Column(db.Integer, primary_key=True, nullable=False)
	area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=False)
	area_name = db.Column(db.String(255), nullable=False)
	base_total = db.Column(db.Integer, nullable=False)
	crawled_at = db.Column(db.DateTime, nullable=False)

	def __repr__(self):
		return '<UtahBaseTotals (%r, %r, %r)>' % (self.area_name, self.base_total, self.crawled_at)

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