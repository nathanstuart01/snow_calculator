from flask import jsonify, request
from app import app
from app.models import UtahBaseTotals, UtahTwentyFourHourTotals

@app.route('/api/v1/basetotals/')
def get_base_totals():
	if request.method == 'GET':
		bases_data = UtahBaseTotals.query.all()
		base_totals_data = []

		for base_data in bases_data:
			obj = {
					'area_name': base_data.area_name,
					'base_total': base_data.base_total,
					'crawled_at': base_data.crawled_at.strftime("%Y-%m-%d")
			}
			base_totals_data.append(obj) 
			
		response = jsonify(base_totals_data)
		response.status_code = 200
		return response 

@app.route('/api/v1/twentyfourhourtotals/')
def get_twenty_four_hour_totals():
	if request.method == 'GET':
		twenty_fours_data = UtahTwentyFourHourTotals.query.all()
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