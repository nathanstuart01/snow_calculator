import csv

raw_snow_file = 'altasnow70s.csv'

with open(raw_snow_file, 'rb') as f:
	area_snow = []
	reader = csv.reader(f)
	your_list = list(reader)

print(your_list)

