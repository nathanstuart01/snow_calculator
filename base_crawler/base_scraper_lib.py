# items to add to a scrape lib class, which I will import the base crawler and if the 
area I specifiy is in the scraper lib, I will make a function that loops through a dict, key=area value=tag to scrape

based on the matches, I will use the base crawler parent class to scrape the selected tags with, then put those values back into the area, base, 24hr variables

libs for parsed pages,

alta process =

area_to_scrape = requests.get('https://www.alta.com/')
souped_area = BeautifulSoup(area_to_scrape.content, 'html.parser')
base_values = souped_area.find_all(class_="value")
base_values[2]
base_values[3]

class BaseScraperLib():

area_1 = { 'name' : 'alta', 'base_selector' : '"value"', 'twenty_four_hr_selector' : 'tbd' }
area_2 = { 'name' : 'snowbird', 'base_selector' : 'tbd', 'twenty_four_hr_selector' : 'tbd' }

area_selector_library = [area_1, area_2]