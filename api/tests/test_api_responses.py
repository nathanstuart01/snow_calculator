import unittest
import requests
from app.routes import *

class APITests(unittest.TestCase):

	test_data = 

	def test_base_data_response(self):
		response = requests.get('http://localhost:5000/api/v1/basedata/')
		self.assertEqual(response.status_code, 200)	

	def test_twenty_four_hour_data_response(self):
		response = requests.get('http://localhost:5000/api/v1/twentyfourhourdata/')
		self.assertEqual(response.status_code, 200)


	def test_base_area_data_response(self):
		area_names = [
			'alta',
			'snowbird',
			'brighton',
			'solitude',
			'park city',
			'deer valley',
			'snowbasin',
			'powder mountain',
			'beaver mountain',
			'cherry peak',
			'brian head',
			'eagle point',
			'sundance',
			'nordic valley',
			]
		for name in area_names:
			response = requests.get('http://localhost:5000/api/v1/basedata/name'+name)
			self.assertEqual(response.status_code, 200)

	def test_twenty_four_hour_area_data_response(self):
		area_names = [
			'alta',
			'snowbird',
			'brighton',
			'solitude',
			'park city',
			'deer valley',
			'snowbasin',
			'powder mountain',
			'beaver mountain',
			'cherry peak',
			'brian head',
			'eagle point',
			'sundance',
			'nordic valley',
			]
		for name in area_names:
			response = requests.get("http://localhost:5000/api/v1/twentyfourhourdata/"+name)
			self.assertEqual(response.status_code, 200)

	def test_base_data_response(self):
		# want to write a test to make sure that the return response of this function is equal to a jsonify object
		self.assertEqual(get_base_totals(), test_data):



if __name__=='__main__':
	unittest.main()

