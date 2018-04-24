from flask import jsonify, request
from app import app
from app.models import UtahBaseTotals

## Query the database for all base totals
## loop through them??
## convert them into a json object with {'id': 'area_id', 'area_name': 'name', 'base_total': 'total', 'crawled_at': 'date'}
## loop thgrough json object and display current totals for current date as a graph
## get base_totals as a variable from the db
## turn that db variable into a json object
@app.route('/api/v1.0/basetotals/')
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
