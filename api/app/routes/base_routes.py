from flask import jsonify, request
from app import app
from app.models.base_data_model import UtahBaseTotals 
from sqlalchemy import asc
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

@app.route('/api/v1/basedata/')
def get_base_totals():
	date = datetime.datetime.today().strftime('%Y-%m-%d')
	client_key = request.headers.get('API-Key')
	SERVER_API_KEY = os.getenv('SERVER_API_KEY')
	if request.method == 'GET':
		if client_key != SERVER_API_KEY:
			response = jsonify('Unauthorized request')
			response.status_code = 401
		bases_data = UtahBaseTotals.query.filter_by(crawled_at=date).order_by(asc(UtahBaseTotals.area_name)).all()
		base_totals_data = []

		for base_data in bases_data:
			obj = {
					'area_id': base_data.area_id,
					'area_name': base_data.area_name.title(),
					'base_total': base_data.base_total,
					'crawled_at': base_data.crawled_at.strftime("%Y-%m-%d")
			}
			base_totals_data.append(obj) 
			
		response = jsonify(base_totals_data)
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.status_code = 200
	return response 
