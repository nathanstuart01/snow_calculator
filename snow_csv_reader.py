import csv

raw_snow_file = 'altasnow70s.csv'

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
	

snow_years, snow_inches = snow_csv_stats_to_array(raw_snow_file)

print(snow_years)
print(snow_inches)


