from areas_crawler import AreasCrawler 
from scraper_lib import ScraperLib
import csv
import datetime
import psycopg2
import time

class GatherSnowStats():

	def __init__(self, stat_type):
		self.stat_type = stat_type

	def crawl_base_data(self):
		base_names = []	
		base_totals = []
		areas = ScraperLib('all areas')
		area_info = areas.area_selector_library
		i = 0
		while i < 14:
			ski_area = AreasCrawler(area_info[i]['name'], area_info[i]['url'])
			ski_area_base = ski_area.get_base_total(ski_area.area_url, area_info[i]['base_selector'], area_info[i]['base_selector_index'])
			base_names.append(ski_area.area_name)	
			base_totals.append(ski_area_base)
			i = i + 1
		base_data = dict(zip(base_names, base_totals))
		return base_data

	def crawl_24_hr_data(self):
		twenty_four_hr_names = []
		twenty_four_hr_totals = []
		areas = ScraperLib('all areas')
		area_info = areas.area_selector_library
		i = 0
		while i < 14:
			ski_area = AreasCrawler(area_info[i]['name'], area_info[i]['url'])
			ski_area_24_hr_total = ski_area.get_24_hr_total(ski_area.area_url, area_info[i]['twenty_four_hr_selector'], area_info[i]['twenty_four_hr_index'])
			twenty_four_hr_names.append(ski_area.area_name)
			twenty_four_hr_totals.append(ski_area_24_hr_total)
			i = i + 1
		twenty_four_hr_data = dict(zip(twenty_four_hr_names, twenty_four_hr_totals))
		return twenty_four_hr_data

	def save_data_to_file(self, data_to_save):
		current_time = datetime.datetime.now().strftime("%Y-%m-%d")
		if data_to_save == 'base':
			base_data = self.crawl_base_data()
			base_file = open('bases.csv', 'w+')
			base_file_writer = csv.writer(base_file)
			for i, (key, value) in enumerate(base_data.items()):
				base_file_writer.writerow([i +1, key, value, current_time])	
			base_file.close()
			self.save_data_to_db('bases.csv')	
			print('base data has been crawled and is saved to a file')
		elif data_to_save == '24hr':
			twenty_four_hr_data = self.crawl_24_hr_data()
			twenty_four_hour_file = open("24hrtotals.csv", "w+")
			twenty_four_hour_file_writer = csv.writer(twenty_four_hour_file)
			for i, (key, value) in enumerate(twenty_four_hr_data.items()):
				twenty_four_hour_file_writer.writerow([i +1, key, value, current_time])				
			twenty_four_hour_file.close()
			self.save_data_to_db('24hrtotals.csv')
			print('24 hr data has been crawled and is saved to a file')
		else:
			print("No other data type to save yet")	

	def save_data_to_db(self, file):
		conn = psycopg2.connect("host=localhost dbname=utahskiareas user=postgres")
		cur = conn.cursor()
		with open(file, 'r') as f:
			if self.stat_type == 'base':
				cur.copy_from(f, 'base_totals', columns=('area_id', 'area_name', 'base_total', 'crawled_at'), sep=',')
				print('base data has been saved to db')
			else:				
				cur.copy_from(f, 'twenty_four_hour_totals', columns=('area_id', 'area_name', 'twenty_four_hour_total', 'crawled_at'), sep=',')
				print('24hr data has been saved to db')
		conn.commit()
		conn.close()

base_data = GatherSnowStats('base')
twenty_four_hour_data = GatherSnowStats('24hr')
base_data.save_data_to_file(base_data.stat_type)
twenty_four_hour_data.save_data_to_file(twenty_four_hour_data.stat_type)
print("Data for bases and 24hrs saved to db, check the appropriate db for data")









