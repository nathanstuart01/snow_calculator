from areas_crawler import AreasCrawler 
from scraper_lib import ScraperLib


class GatherSnowStats():

	def __init__(self, stat_type):
		self.stat_type = stat_type

	def crawl_data(self, data_to_gather):
		base_names = []	
		base_totals = []
		data_to_gather = self.stat_type
		if data_to_gather == 'base':
			areas = ScraperLib('all areas')
			area_info = areas.area_selector_library
			i = 0
			while i < 14:
				ski_area = AreasCrawler(area_info[i]['name'], area_info[i]['url'])
				ski_area_base = ski_area.get_base_total(ski_area.area_url, area_info[i]['base_selector'], area_info[i]['base_selector_index'])
				base_names.append(ski_area.area_name)	
				base_totals.append(ski_area_base)
				i = i + 1
		else:
			print('No data yet to gather besides base data')

		base_data = dict(zip(base_names, base_totals))
		return base_data


base_data_gatherer = GatherSnowStats('base')
print(base_data_gatherer.crawl_data(base_data_gatherer.stat_type))









