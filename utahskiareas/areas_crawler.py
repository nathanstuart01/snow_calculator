import requests 
import re
from bs4 import BeautifulSoup
from scraper_lib import ScraperLib

class AreasCrawler(ScraperLib):

	"""A base crawler class for all ski areas"""
	def __init__(self, area_name):
		super().__init__()
		self.area_name = area_name

	def get_base_total(self, area_url, base_selector, base_selector_index):
		area_to_scrape = requests.get(area_url)
		souped_area = BeautifulSoup(area_to_scrape.content, 'html.parser')
		base_values = souped_area.find_all(class_=base_selector)[base_selector_index].text.encode('utf-8')
		base_total = base_values.decode("ascii", "ignore").replace('"', '')
		self.base_total = int(base_total)
	
	def get_24_hr_total(self, area_url, twenty_four_hour_selector, twenty_four_hour_index):
		area_to_scrape = requests.get(area_url)
		souped_area = BeautifulSoup(area_to_scrape.content, 'html.parser')
		twenty_four_values = souped_area.find_all(class_=twenty_four_hour_selector)[twenty_four_hour_index].text.encode('utf-8')
		twenty_four_total = twenty_four_values.decode("ascii", "ignore").replace('"', '').lower()
		if 'tr' in twenty_four_total:
			self.twenty_four_hour_total = 0
		else:
			self.twenty_four_hour_total = int(twenty_four_total) 
		return self.twenty_four_hour_total

	def scrape_sundance(self, stats_api):
		sundance_api = requests.get(stats_api)
		sundance_data = sundance_api.json()
		sundance_base = sundance_data[0]['base']
		sundance_24_hr = sundance_data[0]['24_hour']
		return sundance_base, sundance_24_hr


	