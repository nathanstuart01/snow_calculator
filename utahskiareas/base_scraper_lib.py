# items to add to a scrape lib class, which I will import the base crawler and if the 
area I specifiy is in the scraper lib, I will make a function that loops through a dict, key=area value=tag to scrape

based on the matches, I will use the base crawler parent class to scrape the selected tags with, then put those values back into the area, base, 24hr variables


class BaseScraperLib():

area_dict_template = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}	

area_1 = { 
			'name' : 'alta', 
			'url': 'https://www.alta.com/', 
			'base_selector' : 'value',
			'base_selector_index' : '[3].contents',
			'twenty_four_hr_selector': 'value',
			'twenty_four_hr_index' : '[2].contents',
			}

area_2 = { 
			'name' : 'snowbird', 
			'url': 'https://www.snowbird.com/', 
			'base_selector' : "sb-condition_value", 
			'base_selector_index' : '[4].text',
			'twenty_four_hr_selector': 'sb-condition_value',
			'twenty_four_hr_index' : '[2].text', 
			}

area_selector_library = [area_1, area_2]

def process_area_to_scrape(area):
	#call the area in its index from the area selector library
	# define the values of each areas dict to scrape
	# THis is to prepare the varaiables to then call in the gather_snow_Stats_script 
	# How can i access to area selector libray, to then passo on the specific info to the gather snow stats function 

