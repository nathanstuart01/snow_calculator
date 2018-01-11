from areas_crawler import AreasCrawler 
from scraper_lib import ScraperLib

#alta_crawl = AreasCrawler('Alta', '', '' )
#alta_base = alta_crawl.get_base_total('https://www.alta.com/')
#snowbird_crawl = AreasCrawler('Snowbird', '', '')
#snowbird_base = snowbird_crawl.get_base_total('https://www.snowbird.com/')
#brighton_crawl = AreasCrawler('Solitude', '', '')
#brighton_24hr = brighton_crawl.get_base_total('https://solitudemountain.com/') 
#park_city_crawl = AreasCrawler('Park City', '', '')
#park_city_snow_data = park_city_crawl.scrape_park_city('https://www.parkcitymountain.com/the-mountain/mountain-conditions/snow-and-weather-report.aspx')
#print(park_city_snow_data)
area_selectors = ScraperLib()
print(area_selectors.area_selector_library[1:4])