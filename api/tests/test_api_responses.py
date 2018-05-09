import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
import unittest
import json 
from flask import jsonify, request
from app import app
from app.models.base_data_model import UtahBaseTotals 
from sqlalchemy import asc
import requests

class APITests(unittest.TestCase):

	
	def setUp(self):
		"""define test variables and initialize app """
		self.app = app.test_client()
		self.app.test = True
		self.base_data = [
				
				{
				"area_name": "alta",
				"base_total": 98,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "beaver mountain",
				"base_total": 68,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "brian head",
				"base_total": 40,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "brighton",
				"base_total": 77,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "cherry peak",
				"base_total": 44,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "deer valley",
				"base_total": 67,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "eagle point",
				"base_total": 19,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "nordic valley",
				"base_total": 12,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "park city",
				"base_total": 50,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "powder mountain",
				"base_total": 51,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "snowbasin",
				"base_total": 64,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "snowbird",
				"base_total": 103,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "solitude",
				"base_total": 75,
				"crawled_at": "2018-03-05"
				},
				{
				"area_name": "sundance",
				"base_total": 36,
				"crawled_at": "2018-03-05"
				}
		]


	def test_home_page_message(self):
		result = self.app.get('/')
		self.assertEqual(result.data, str.encode("Home page for all the Utah snow information you need to know"))	

	def test_base_data_response(self):
		response = requests.get('http://localhost:5000/api/v1/basedata/')
		self.assertEqual(response.status_code, 200)	

	def test_base_data_get_request(self):
		response = requests.get('http://localhost:5000/api/v1/basedata/')
		self.assertEqual(json.loads(response.content), self.base_data)

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

	"""def test_base_data_response(self):
		# want to write a test to make sure that the return response of this function is equal to a jsonify object
		test_data = 
		self.assertEqual(get_base_totals(), test_data):

"""

if __name__=='__main__':
	unittest.main()

