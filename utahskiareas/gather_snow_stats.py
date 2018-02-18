from areas_crawler import AreasCrawler 
from scraper_lib import ScraperLib

"""This is going to be the getter/parser class"""
#get all the info I want to crawl the bases
#use the scraper lib
#create an instance with access to each scraper lib area
#make a varible 

scrape_info = ScraperLib()

#loop through all the areas in scrape_info
#assign each area name, url, base info, selector as a variable
#use those assigned variables as instancers of a areas_crawler class
#print those instances results, eventually this would save to a temp file

def get_base_info(area_selector_library):
	return area_selector_library

print(get_base_info(scrape_info.area_selector_library)) 






