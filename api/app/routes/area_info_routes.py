from flask import jsonify, request
from app import app
from app.models.area_name_data_model import UtahSkiAreas 
from sqlalchemy import asc

@app.route('/api/v1/areainfodata/')
def get_areas_info():
	if request.method == 'GET':
		#create a query within in here that gets the current date of base data only, makes each area clickable to go to history of all base data totals for that area
		areas_data = UtahSkiAreas.query.order_by(asc(UtahSkiAreas.area_name)).all()
		areas_info_data = []

		for area_data in areas_data:
			obj = {
					'area_name': area_data.area_name
			}
			areas_info_data.append(obj) 
			
		response = jsonify(areas_info_data)
		response.status_code = 200
		return response 

@app.route('/api/v1/areainfodata/<single_area_info_data>')
def get_single_area_info(single_area_info_data):
	#Gets specific areas base totals
	if request.method == 'GET':
		single_area_data = UtahSkiAreas.query.filter_by(area_name=single_area_info_data).all()
		single_area_info_data = []
		for data in single_area_data:
			single_area_data_obj = {
							'area_name': data.area_name
						}
			single_area_info_data.append(single_area_data_obj)

		response = jsonify(single_area_info_data)
		response.status_code = 200
		return response