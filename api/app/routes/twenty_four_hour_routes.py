from flask import jsonify, request
from app import app
from app.models.twenty_four_hour_data_model import UtahTwentyFourHourTotals
from sqlalchemy import asc
import datetime
import os
from dotenv import load_dotenv
import datetime
from datetime import datetime,timedelta

load_dotenv()


@app.route('/api/v1/twentyfourhourdata/')
def get_twenty_four_hour_totals():
	date = datetime.now() - timedelta(hours=7)
	date = current_time.strftime("%Y-%m-%d")
	client_key = request.headers.get('API-Key')
	client_ip = request.headers.get('ip')
	SERVER_API_KEY = os.getenv('SERVER_API_KEY')
	if client_key != SERVER_API_KEY:
		response = jsonify('Unauthorized request')
		response.status_code = 401
		return response
	if request.method == 'GET':
		twenty_fours_data = UtahTwentyFourHourTotals.query.filter_by(crawled_at=date).order_by(asc(UtahTwentyFourHourTotals.area_name)).all()
		twenty_four_totals_data = []

		for twenty_four_data in twenty_fours_data:
			obj = {
					'area_name': twenty_four_data.area_name.title(),
					'twenty_four_hour_total': twenty_four_data.twenty_four_hour_total,
					'crawled_at': twenty_four_data.crawled_at.strftime("%Y-%m-%d")
			} 
			twenty_four_totals_data.append(obj)

		response = jsonify(twenty_four_totals_data)
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.status_code = 200
		return response
