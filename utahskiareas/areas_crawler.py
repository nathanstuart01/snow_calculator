import requests 
import re
from bs4 import BeautifulSoup
#check to see if I need to import file/class/methods from 

class AreasCrawler():
	"""A base crawler for all ski areas"""
	def __init__(self, area_name):
		self.area_name = area_name
		self.base_total = base_total
		self.twenty_four_hour_total = twenty_four_hour_total

	def get_base_total(self, area_url):
		area_to_scrape = requests.get(area_url)
		souped_area = BeautifulSoup(area_to_scrape.content, 'html.parser')
		base_values = souped_area.find_all(base_values_selector)
		base_selector = base_values + base_data_selector
		base_total = base_selector
		return base_total

		# not finished 
	def scrape_park_city(self, area_url):
		park_city_scraped = requests.get(area_url)
		park_city_souped = BeautifulSoup(park_city_scraped.content, 'html.parser')
		park_city_values = park_city_souped.find_all('script', type='text/javascript')[1]
		park_city_string = park_city_values.contents[0]
		park_city_snow_data_searcher = re.compile(r'Inches\S\S\S\d+')
		park_city_snow_data = park_city_snow_data_searcher.findall(park_city_string) 
		park_city_base_raw = park_city_snow_data[4]
		park_city_24hr_raw = park_city_snow_data[1]
		park_city_base = park_city_base_raw.replace('Inches":"', '')
		park_city_24hr = park_city_24hr_raw.replace('Inches":"', '')
		return park_city_base, park_city_24hr


	def scrape_sundance(self, stats_api):
		sundance_api = requests.get(stats_api)
		sundance_data = sundance_api.json()
		sundance_base = sundance_data[0]['base']
		sundance_24_hr = sundance_data[0]['24_hour']
		return sundance_base, sundance_24_hr


	