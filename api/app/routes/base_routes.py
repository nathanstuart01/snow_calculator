from flask import jsonify, request
from app import app
from app.models.base_data_model import UtahBaseTotals 
from sqlalchemy import asc

@app.route('/api/v1/basedata/')
def get_base_totals():
	if request.method == 'GET':
		#create a query within in here that gets the current date of base data only, makes each area clickable to go to history of all base data totals for that area
		bases_data = UtahBaseTotals.query.order_by(asc(UtahBaseTotals.area_name)).all()
		base_totals_data = []

		for base_data in bases_data:
			obj = {
					'area_id': base_data.area_id,
					'area_name': base_data.area_name,
					'base_total': base_data.base_total,
					'crawled_at': base_data.crawled_at.strftime("%Y-%m-%d")
			}
			base_totals_data.append(obj) 
			
		response = jsonify(base_totals_data)
		response.status_code = 200
		return response 

@app.route('/api/v1/basedata/<area_base_totals>')
def get_area_base_total(area_base_totals):
	#Gets specific areas base totals
	if request.method == 'GET':
		area_base_data = UtahBaseTotals.query.filter_by(area_name=area_base_totals).all()
		area_data = []
		for data in area_base_data:
			area_data_obj = {
							'area_id': base_data.area_id,
							'area_name': data.area_name,
							'base_total': data.base_total,
							'crawled_at': data.crawled_at.strftime("%Y-%m-%d")
						}
			area_data.append(area_data_obj)

		response = jsonify(area_data)
		response.status_code = 200
		return response