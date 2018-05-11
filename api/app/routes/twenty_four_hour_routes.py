from flask import jsonify, request
from app import app
from app.models.twenty_four_hour_data_model import UtahTwentyFourHourTotals
from sqlalchemy import asc

@app.route('/api/v1/twentyfourhourdata/')
def get_twenty_four_hour_totals():
	if request.method == 'GET':
		#create a query within in here that gets the current date of twenty four hour data only, makes each area clickable to go to history of all twenty four hour data totals for that area
		twenty_fours_data = UtahTwentyFourHourTotals.query.filter_by(crawled_at='2018-03-05').order_by(asc(UtahTwentyFourHourTotals.area_name)).all()
		twenty_four_totals_data = []

		for twenty_four_data in twenty_fours_data:
			obj = {
					'area_name': twenty_four_data.area_name,
					'twenty_four_hour_total': twenty_four_data.twenty_four_hour_total,
					'crawled_at': twenty_four_data.crawled_at.strftime("%Y-%m-%d")
			} 
			twenty_four_totals_data.append(obj)

		response = jsonify(twenty_four_totals_data)
		response.status_code = 200
		return response

@app.route('/api/v1/twentyfourhourdata/<area_twenty_four_hour_totals>')
def get_area_twenty_four_hour_total(area_twenty_four_hour_totals):
	#Gets specific areas base totals
	if request.method == 'GET':
		area_twenty_four_hour_data = UtahTwentyFourHourTotals.query.filter_by(crawled_at='2018-03-05').filter_by(area_name=area_twenty_four_hour_totals).all()
		area_data = []
		for data in area_twenty_four_hour_data:
			area_data_obj = {
							'area_name': data.area_name,
							'twenty_four_hour_total': data.twenty_four_hour_total,
							'crawled_at': data.crawled_at.strftime("%Y-%m-%d")
						}
			area_data.append(area_data_obj)

		response = jsonify(area_data)
		response.status_code = 200
		return response