import csv

def snow_csv_stats_to_array(snow_csv_file):
	snow_years = []
	snow_inches = []

	with open(snow_csv_file, 'r') as csv_snow_data:
	    csv_reader = csv.reader(csv_snow_data)
	    for row in csv_reader:
	        snow_years.extend(row[0:1]) 
	        snow_inches.extend(row[1:2])
	        
	snow_years.pop(0)
	snow_inches.pop(0)
	snow_years_int = [ int(x) for x in snow_years ]
	snow_inches_int = [ int(x) for x in snow_inches ]

	return snow_years_int, snow_inches_int



# either add in a class next or another function that takes csv lists from above, calcualtes mean, std of snowfall stats, then graphs out data
#make this a module that is part of a class for calculating snowfall statistics
# calculate mean/ standard deviation of snow inches
# use scrapy to crawl a bunch of different ski areas i am intersted in, turn their base into a graph that shows which one has the most
# save the totals to a db each day
# have spiders crawl daily
# have another graph taht calculates 24 hr snow based on daily totals - yesterdays totals
# add the difference to a total snowfall for each year db
# display data source information of where snow is measured


