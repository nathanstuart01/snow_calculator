from areas_crawler import AreasCrawler 
from scraper_lib import ScraperLib


# want to be able to have a list of all my area names
# I want to be able to send off a job each day that gathers their data
# I want to be able to saved that gathered data to a db for that areaa
# I want to use the classes from above to do this


# loop through the areas
# for each area, fire off the method to get that areas data
# save that areas data to a db
# will need the data from the scraper lib to know what to crawl
# will need the methods to crawl each area from the areas_crawler
# make a loop, and depednding on the name of that area in the loop, that is the method I call, and I pass in the area selectors to each method


#def get_area_selectors(areas):
#	for area in areas:
		# I have access to my selectors
		# I want to get the base selectors and send those to their appropriate function to gather the data for
		# I need to write the methods for each areas base selector
		# I will import the areas crawler class and send the correct selectors to the correct methods to scrape, making objects from the for loop to do that



			# set area name as a variable to pass to the function to use to select data with, function selects base/24hr
			# for a for i in loop here to loop through as many times as the length of the area seletor lib

#def get_base_24hr_totals_park_city(park_city_base_selector, park_city_24hr_selector):
	# use the variables I created in the get area names
	# create a crawl functdion here with the selectors to gather the data
	# set those data gathered to a variable that I can then use to save to the specific db for that area

#def save_base_24hr_totals_park_city(park_city_base_total, park_city_24hr_total):
	#take the totals I crawled from the above function, save them to a database
	# the entry will correspond to the ski areas unique id
	# the entry will up made as a new one each day
alta = AreasCrawler('alta', 'https://alta.com')
print(alta.area_selector_library[2])






