import requests 
import logging
from bs4 import BeautifulSoup
#check to see if I need to import file/class/methods from 

class AreasCrawler():
	"""A base crawler for all ski areas"""
	def __init__(self, area_name, base_total, twenty_four_hour_total):
		self.area_name = area_name
		self.base_total = base_total
		self.twenty_four_hour_total =twenty_four_hour_total

	def get_base_total(self, area_url):
		area_base_selectors = "value"
		area_to_scrape = requests.get(area_url)
		souped_area = BeautifulSoup(area_to_scrape.content, 'html.parser')
		base_values = souped_area.find_all(class_=area_base_selectors)
		base_selector = base_values[3].contents
		base_total = base_selector
		return base_total

	# write another function that returns 24 hr total
