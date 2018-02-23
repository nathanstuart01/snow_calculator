from areas_crawler import AreasCrawler 
from scraper_lib import ScraperLib

"""This is going to be the getter/parser class"""
#get all the info I want to crawl the bases
#use the scraper lib
#create an instance with access to each scraper lib area
#make a varible 

def create_area_to_crawl():
	areas = ScraperLib('all areas')
	area_info = areas.area_selector_library
	i = 0
	while i < 5:
		ski_area = AreasCrawler(area_info[i]['name'], area_info[i]['url'])
		ski_area_base = ski_area.get_base_total(ski_area.area_url, area_info[i]['base_selector'], area_info[i]['base_selector_index'])
		print(ski_area_base, ski_area.area_name)
		i = i + 1


print(create_area_to_crawl())

#loop through all the areas in scrape_info
#assign each area name, url, base info, selector as a variable
#use those assigned variables as instancers of a areas_crawler class
#print those instances results, eventually this would save to a temp file




#def get_base_info(area_name):
#	if area_name == 'alta':
#		alta_scrape = AreasCrawler
#	return area_selector_library

#print(get_base_info(scrape_info.area_selector_library)) 






