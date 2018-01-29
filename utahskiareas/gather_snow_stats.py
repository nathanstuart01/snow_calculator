from areas_crawler import AreasCrawler 
from scraper_lib import ScraperLib

alta = AreasCrawler('alta')
print(alta.get_base_total('https://wwww.alta.com', 'value', 3))
print(alta.get_24_hr_total('https://wwww.alta.com', 'value', 2))

snowbird= AreasCrawler('snowbird')
print(snowbird.get_base_total('https://www.snowbird.com/', "sb-condition_value", 4))
print(snowbird.get_24_hr_total('https://www.snowbird.com/', "sb-condition_value", 2))







