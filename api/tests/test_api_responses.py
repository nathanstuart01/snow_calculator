import unittest
import requests

class APITests(unittest.TestCase):

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


if __name__=='__main__':
	unittest.main()

