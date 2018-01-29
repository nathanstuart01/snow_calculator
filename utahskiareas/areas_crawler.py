import requests 
import re
from bs4 import BeautifulSoup
from scraper_lib import ScraperLib

class AreasCrawler(ScraperLib):

	"""A base crawler class for all ski areas"""
	def __init__(self, area_name):
		super().__init__()
		self.area_name = area_name
		self.base_total = 0
		self.twenty_four_hour_total = 0

	# do this as a for loop and each time craete a new variable, could it be a new class instance variable?
		
	# for example in the area, make self.base_total_alta a variable to be used as a class property
	def get_base_total(self, area_url, base_selector, base_selector_index):
		area_to_scrape = requests.get(area_url)
		souped_area = BeautifulSoup(area_to_scrape.content, 'html.parser')
		base_values = souped_area.find_all(class_=base_selector)[base_selector_index].text.encode('utf-8')
		return base_values.decode("ascii", "ignore")


		#use if/else logic to determine what area to select
	def get_24_hr_total(self, area_url, twenty_four_hour_selector):
		area_to_scrape = requests.get(area_url)
		souped_area = BeautifulSoup(area_to_scrape.content, 'html.parser')
		base_values = souped_area.find_all(class_=twenty_four_hour_selector)[2].text.encode('utf-8')
		twenty_four_hour_total = base_values.decode("ascii", "ignore").replace('"', '')
		twenty_four_hour_total_to_int = int(twenty_four_hour_total)
		self.twenty_four_hour_total = twenty_four_hour_total_to_int
		return self.twenty_four_hour_total


		 # incorporate this into one function above, using if
		"""def park_city(self, area_url):
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
		"""
		# api scraper(if that is such a thing?)getter?
	def scrape_sundance(self, stats_api):
		sundance_api = requests.get(stats_api)
		sundance_data = sundance_api.json()
		sundance_base = sundance_data[0]['base']
		sundance_24_hr = sundance_data[0]['24_hour']
		return sundance_base, sundance_24_hr


	