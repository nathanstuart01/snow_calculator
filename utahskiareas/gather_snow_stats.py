from areas_crawler import AreasCrawler 
from scraper_lib import ScraperLib
import csv
import datetime
import psycopg2

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
			base_file = csv.writer(open("bases.csv", "w+"))
			for i, (key, value) in enumerate(base_data.items()):
				base_file.writerow([i +1, key, value, current_time])	
			self.save_data_to_db("bases.csv")
		elif data_to_save == '24hr':
			twenty_four_hr_data = self.crawl_24_hr_data()
			twenty_four_hour_file = csv.writer(open("24hrtotals.csv", "w+"))
			for i, (key, value) in enumerate(twenty_four_hr_data.items()):
				twenty_four_hour_file.writerow([i +1, key, value, current_time])	
			self.save_data_to_db("24hrtotals.csv")
		else:
			print("No other data type to save yet")

	def save_data_to_db(self, file):
		conn = psycopg2.connect("host=localhost dbname=utahskiareas user=postgres")
		cur = conn.cursor()
		f = open(file, 'r')
		cur.copy_from(f, 'twenty_four_hour_totals', columns=('area_id', 'area_name', 'twenty_four_hour_total', 'crawled_at'), sep=',')
		conn.commit()
		conn.close()

#base_data = GatherSnowStats('base')
twenty_four_hour_data = GatherSnowStats('24hr')
#base_data.save_data_to_file(base_data.stat_type)
twenty_four_hour_data.save_data_to_db('24hrtotals.csv')
#base_data.save_data_to_db('bases.csv')
print("Data saved to db, check the appropriate db for data")









