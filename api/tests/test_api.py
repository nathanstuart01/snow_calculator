import unittest
import requests

class APITests(unittest.TestCase):

	def test_base_data_response(self):
		response = requests.get('http://localhost:5000/api/v1/basedata/')
		self.assertEqual(response.status_code, 200)	

	def test_twenty_four_hour_data_response(self):
		response = requests.get('http://localhost:5000/api/v1/twentyfourhourdata/')
		self.assertEqual(response.status_code, 200)

		#re-write this test and one below to loop through each area and make a request to each area, ensuring all areas can be requested
	def test_base_area_data_response(self):
		response = requests.get('http://localhost:5000/api/v1/basedata/alta')
		self.assertEqual(response.status_code, 200)

		#re-write this test and one below to loop through each area and make a request to each area, ensuring all areas can be requested
	def test_twenty_four_hour_area_data_response(self):
		response = requests.get('http://localhost:5000/api/v1/twentyfourhourdata/alta')
		self.assertEqual(response.status_code, 200)

if __name__=='__main__':
	unittest.main()

