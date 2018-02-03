from areas_crawler import AreasCrawler 
from scraper_lib import ScraperLib


"""Below are the areas I have already crawled using the get base total class method"""

#snowbasin = AreasCrawler('snowbasin')

#print(snowbasin.get_base_total('https://www.snowbasin.com/', "snow-report-grid", "right"))

#powder_mountain = AreasCrawler('powder_mountain')
#print(powder_mountain.get_base_total('http://www.powdermountain.com/en/', "gmad-third-col", 2))

#beaver_mountain = AreasCrawler('beaver_mountain', 'http://www.skithebeav.com/')
#print(beaver_mountain.get_base_total(beaver_mountain.area_url, 'td', 3))

#cherry_peak = AreasCrawler('cherry_peak', 'http://skicherrypeak.com/rpt/?snow-report')
#print(cherry_peak.get_base_total(cherry_peak.area_url, 'Normal_text', 5))

brian_head = ScraperLib()
 
brian_head_crawl = AreasCrawler('brian_head', brian_head.area_selector_library[10]['url'])

#print(brian_head_crawl.get_base_total(brian_head_crawl.area_url, brian_head.area_selector_library[10]['base_selector'], 0))

#print(brian_head.area_selector_library[10]['base_selector'])

print(brian_head_crawl.get_base_total(brian_head_crawl.area_url, 'text-left', 7))




