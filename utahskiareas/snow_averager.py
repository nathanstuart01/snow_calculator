import numpy as np
from scipy import stats 

Altasnow70s = [481,466,496,595,605,439,314,524,488,514]
Altasnow80s = [391,696,637,743,457,599,381,410,581,448]
Altasnow90s = [580,395,650,490,745,562,599,574,458,446]
Altasnow20s = [469,567,399,570,553,633,356,654,578,430]
Altasnow21s = [553,329,382,357,267,393]
AltaAverages = []
AltaRawTotals = []
ski_area = 'Alta'




# Make average of yearly snowfall for all areas in PNW/Utah/Jackson
# Take stan dev of yearly snowfall and determine the swing in each year 

def snow_averager(array1,array2,array3,array4,array5):
    snow70 = np.average(array1)
    snow80 = np.average(array2)
    snow90 = np.average(array3)
    snow20 = np.average(array4)
    snow21 = np.average(array5)
    AltaAverages.extend([snow70, snow80, snow90, snow20, snow21])
    AltaRawTotals.extend([Altasnow70s, Altasnow80s, Altasnow90s, Altasnow20s, Altasnow21s])

    print("The average snowfall at Alta in the 70's was " + str(snow70) + " inches.")
    print("The average snowfall at Alta in the 80's was " + str(snow80) + " inches.")
    print("The average snowfall at Alta in the 90's was " + str(snow90) + " inches.")
    print("The average snowfall at Alta in the 20's was " + str(snow20) + " inches.")
    print("The average snowfall at Alta in the 21's was " + str(snow21) + " inches.")
    snowfall_range_decades(AltaAverages)


def snowfall_range_decades(array):
	area_snowfall_decade_average = np.mean(array)
	area_snowfall_variation = np.std(array)
	print("The average annual snowfall every year at " + ski_area + " over the past five decades is: " + str(area_snowfall_decade_average))
	print("The variation in average annual snowfall every year at " + ski_area + 
	" over the past five decades is: " + str(area_snowfall_variation) + "in.\nWhere will you ski at?")
	snowfall_std(AltaRawTotals)

def snowfall_std(array):
	snow_stats_flatten = np.concatenate(array)
	snow_mean = np.mean(snow_stats_flatten)
	snow_std = np.std(snow_stats_flatten)
	# Eventually make a dictionary that has year and snowfall, then sort through those years and match up years that are outside of 1 std of the mean and above 1 std of the mean

	print("The snowfall years that are outside 1 STD of mean are greater than or less than: " + str(snow_std) + "in more or less than " + str(snow_mean) + "in.")

snow_averager(Altasnow70s, Altasnow80s, Altasnow90s, Altasnow20s, Altasnow21s)