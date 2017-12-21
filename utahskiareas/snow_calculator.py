import snow_csv_reader


#Put in the name of the file you want to calculate
raw_snow_file = 'altasnow70s.csv'

#Call the function to put csv stats into lists for future calculations
snow_years, snow_inches = snow_csv_reader.snow_csv_stats_to_array(raw_snow_file)

print(snow_years)
print(snow_inches)
