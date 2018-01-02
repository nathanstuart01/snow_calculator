# items to add to a scrape lib class, which I will import the base crawler and if the 
# area I specifiy is in the scraper lib, I will make a function that loops through a dict, key=area value=tag to scrape

#based on the matches, I will use the base crawler parent class to scrape the selected tags with, then put those values back into the area, base, 24hr variables


#class BaseScraperLib():

area_selector_library = [alta, snowbird]

area_dict_template = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}	

alta = { 
			'name' : 'alta', 
			'url': 'https://www.alta.com/', 
			'base_selector' : '(class_="value")',
			'base_selector_index' : '[3].contents',
			'twenty_four_hr_selector': '(class_="value")',
			'twenty_four_hr_index' : '[2].contents',
			}

snowbird = { 

			'name' : 'snowbird', 
			'url': 'https://www.snowbird.com/', 
			'base_selector' : '(class_="sb-condition_value")', 
			'base_selector_index' : '[4].text',
			'twenty_four_hr_selector': '(class_="sb-condition_value")',
			'twenty_four_hr_index' : '[2].text', 
			}

brighton = {
			'name': 'brighton',
			'url': 'http://www.brightonresort.com/mountain/snow-report/',
			'base_selector': 'find_all("h2")',
			'base_selector_index': '[3].contents[0].replace('"', '')',
			'twenty_four_hr_selector': 'find_all("p")',
			'twenty_four_hr_index': "[3].contents[0].replace('\r\n\t\t\t\t\t\tLast 24hr: ', '').replace('"', '')",
	}

solitude = {
			'name': 'solitude',
			'url': 'https://solitudemountain.com/',
			'base_selector': 'find_all(class_="type")',
			'base_selector_index': '[2].text.replace('Base ', '').replace('"', '')',
			'twenty_four_hr_selector': 'find_all(class_="type")',
			'twenty_four_hr_index': '[0].text.replace('24 Hrs ', '').replace('"', '')',
	}

park_city = {
	'name': 'park city',
	'url': 'https://www.parkcitymountain.com/the-mountain/mountain-conditions/snow-and-weather-report.aspx',
	'base_selector': "soup.find_all('script', type='text/javascript')[1]",
	'base_selector_index': '',
	'twenty_four_hr_selector': "soup.find_all('script', type='text/javascript')[1]",
	'twenty_four_hr_index': '',
	}

deer_valley = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}

snowbasin = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}

powder_mountain = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}

beaver = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}

cherry_peak = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}

brianhead = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}

eagle_point = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}

sundance = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}

nordic_valley = {
	'name': '',
	'url': '',
	'base_selector': '',
	'base_selector_index': '',
	'twenty_four_hr_selector': '',
	'twenty_four_hr_index': '',
	}


def process_area_to_scrape(dict):
	print(dict[1])
	#call the area in its index from the area selector library
	# define the values of each areas dict to scrape
	# THis is to prepare the varaiables to then call in the gather_snow_Stats_script 
	# How can i access to area selector libray, to then passo on the specific info to the gather snow stats function 

process_area_to_scrape(area_selector_library)
