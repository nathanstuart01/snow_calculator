import requests 
import re
import json
from bs4 import BeautifulSoup
from scraper_lib import ScraperLib


class AreasCrawler(ScraperLib):

	"""A base crawler class for all ski areas"""
	def __init__(self, area_name, area_url):
		super().__init__()
		self.area_name = area_name
		self.area_url = area_url
		self.base_total = 0
		self.twenty_four_hour_total = 0


		"""One base cralwer function to rule them all!!!!"""
	def get_base_total(self, area_url, base_selector, base_selector_index):
		area_to_scrape = requests.get(area_url)
		if self.area_name == 'sundance':
			json_data = json.loads(area_to_scrape.content)
			base_values = json_data[base_selector][base_selector_index]
			self.base_total = int(base_values)
			return self.base_total 
		souped_area = BeautifulSoup(area_to_scrape.content, 'html.parser')
		if self.area_name == 'solitude':
			base_values = souped_area.find_all(class_=base_selector)[base_selector_index].text
			base_total = base_values.replace('Base ', '').replace('"', '')
			self.base_total = int(base_total)
			return self.base_total
		elif self.area_name == 'snowbasin':
			base_values = souped_area.find_all(class_=base_selector)[0].contents[base_selector_index].text
			base_total = base_values.replace('Base', '').replace('"', '')
			self.base_total = int(base_total)
			return self.base_total
		elif self.area_name == 'powder_mountain' or self.area_name == 'deer_valley':
			base_values = souped_area.find_all(class_=base_selector)[base_selector_index]
			if self.area_name == 'powder_mountain':
				base_values_specific = base_values.find_all('div')[base_selector_index - 1].text.encode('utf-8')
				base_total = base_values_specific.decode('ascii', 'ignore').replace('BASE', '')
			else:
				base_values_specific = base_values.find_all('div')[base_selector_index + 3].text.encode('utf-8')
				base_total = base_values_specific.decode('ascii', 'ignore').replace('"', '')
			self.base_total = int(base_total)
			return self.base_total
		elif self.area_name == 'beaver_mountain' or self.area_name == 'brighton' or self.area_name == 'nordic valley':
			base_values = souped_area.find_all(base_selector)[base_selector_index].text.encode('utf-8')
			base_total = base_values.decode('ascii', 'ignore').replace('"', '')
			self.base_total = int(base_total)
			return self.base_total
		elif self.area_name == 'cherry_peak':
			base_values = souped_area.find_all(class_=base_selector)[base_selector_index].text.encode('utf-8')
			base_total = base_values.decode('ascii', 'ignore').replace('Snow Base: ', '')
			self.base_total = int(base_total)
			return self.base_total
		elif self.area_name == 'eagle point':
			base_values = souped_area.find_all(class_=base_selector)[base_selector_index].find_all('span')[0].text.encode('utf-8')
			base_total = base_values.decode('ascii', 'ignore').replace('"', '')
			self.base_total = int(base_total)
			return self.base_total
		elif self.area_name == 'park city':
			base_values = souped_area.find_all(base_selector, type='text/javascript')[base_selector_index]
			base_string = str(base_values)
			base_total = re.search('BaseDepth":{"Inches":"\d+\"', base_string)
			self.base_total = int(base_total.group().replace('BaseDepth":{"Inches":"','').replace('"', ''))
			return self.base_total 
		else:
			base_values = souped_area.find_all(class_=base_selector)[base_selector_index].text.encode('utf-8')
			base_total = base_values.decode("ascii", "ignore").replace('"', '')
			self.base_total = int(base_total)
			return self.base_total
	
	def get_24_hr_total(self, area_url, twenty_four_hour_selector, twenty_four_hour_index):
		area_to_scrape = requests.get(area_url)
		if self.area_name == 'sundance':
			json_data = json.loads(area_to_scrape.content)
			twenty_four_hr_values = json_data[twenty_four_hour_selector][twenty_four_hour_index]
			if 'tr' in twenty_four_hr_values:
				self.twenty_four_hour_total = 0
			else:
				self.twenty_four_hour_total = int(twenty_four_hr_values)
			return self.twenty_four_hour_total

		souped_area = BeautifulSoup(area_to_scrape.content, 'html.parser')
		if self.area_name == 'solitude':
			twenty_four_hr_values = souped_area.find_all(class_=twenty_four_hour_selector)[twenty_four_hour_index].text
			twenty_four_hr_total = twenty_four_hr_values.replace("24 Hrs ", '').replace('"', '')
			if 'tr' in twenty_four_hr_total:
				self.twenty_four_hour_total = 0
			else:
				self.twenty_four_hour_total = int(twenty_four_hr_total) 
				return self.twenty_four_hour_total
		elif self.area_name == 'snowbasin':
			twenty_four_hr_values = souped_area.find_all(class_=twenty_four_hour_selector)[0].contents[twenty_four_hour_index].text
			twenty_four_hr_total = twenty_four_hr_values.replace('24 hour ', '').replace('"', '')
			if 'tr' in twenty_four_hr_total:
				self.twenty_four_hour_total = 0
			else:
				self.twenty_four_hour_total = int(twenty_four_hr_total) 
				return self.twenty_four_hour_total

	def test_get_base_total(self, area_url):
		area_to_scrape = requests.get(area_url)
		souped_area = BeautifulSoup(area_to_scrape.content, 'html.parser')
		base_values = souped_area.find_all('script', type='text/javascript')[1]
		base_string = str(base_values)
		base_total = re.search('BaseDepth":{"Inches":"\d+\"', base_string)
		self.base_total = int(base_total.group().replace('BaseDepth":{"Inches":"','').replace('"', ''))
		return self.base_total 
		#to still make one base scraper total, do a if self.area_name == 'Alta'
			#do this
		# if self.area_name == 'Solitude'
			# do this
		#include the different selector and decoder methods associated with each area

	def scrape_sundance(self, stats_api):
		sundance_api = requests.get(stats_api)
		sundance_data = sundance_api.json()
		sundance_base = sundance_data[0]['base']
		sundance_24_hr = sundance_data[0]['24_hour']
		return sundance_base, sundance_24_hr


	