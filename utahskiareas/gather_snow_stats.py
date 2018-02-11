from areas_crawler import AreasCrawler 
from scraper_lib import ScraperLib


"""Below are the areas I have already crawled using the get base total class method"""

snowbasin = AreasCrawler('snowbasin', 'https://www.snowbasin.com/')

print(snowbasin.get_base_total(snowbasin.area_url, "snow-report-grid", 3))
print(snowbasin.get_24_hr_total(snowbasin.area_url, "snow-report-grid", 1))

#powder_mountain = AreasCrawler('powder_mountain', 'http://www.powdermountain.com/en/')
#print(powder_mountain.get_base_total(powder_mountain.area_url, "gmad-third-col", 2))

#beaver_mountain = AreasCrawler('beaver_mountain', 'http://www.skithebeav.com/')
#print(beaver_mountain.get_base_total(beaver_mountain.area_url, 'td', 3))

#cherry_peak = AreasCrawler('cherry_peak', 'http://skicherrypeak.com/rpt/?snow-report')
#print(cherry_peak.get_base_total(cherry_peak.area_url, 'Normal_text', 5))

#brian_head = ScraperLib()
 
#brian_head_crawl = AreasCrawler('brian_head', brian_head.area_selector_library[10]['url'])

#print(brian_head_crawl.get_base_total(brian_head_crawl.area_url, brian_head.area_selector_library[10]['base_selector'], 0))

#print(brian_head.area_selector_library[10]['base_selector'])

#print(brian_head_crawl.get_base_total(brian_head_crawl.area_url, brian_head.area_selector_library[10]['base_selector'], 7))

#brighton = ScraperLib()

#brighton_crawl = AreasCrawler('brighton', brighton.area_selector_library[2]['url'])

#print(brighton_crawl.get_base_total(brighton_crawl.area_url, brighton.area_selector_library[2]['base_selector'], 3))

#deer_valley = ScraperLib()

#deer_valley_crawl = AreasCrawler('deer_valley', deer_valley.area_selector_library[5]['url'])

#print(deer_valley_crawl.get_base_total(deer_valley_crawl.area_url, deer_valley.area_selector_library[5]['base_selector'], 0))

#nordic_valley = ScraperLib()

#print(nordic_valley.area_selector_library[13]['name'])
#nordic_valley_crawl = AreasCrawler(nordic_valley.area_selector_library[13]['name'], nordic_valley.area_selector_library[13]['url'])

#print(nordic_valley_crawl.get_base_total(nordic_valley_crawl.area_url, nordic_valley.area_selector_library[13]['base_selector'], 6))

#eagle_point = ScraperLib()
#eagle_point_crawl = AreasCrawler(eagle_point.area_selector_library[11]['name'], eagle_point.area_selector_library[11]['url'])
#print(eagle_point_crawl.get_base_total(eagle_point_crawl.area_url, eagle_point.area_selector_library[11]['base_selector'], 1))


#sundance = AreasCrawler('sundance', 'https://sheetsu.com/apis/v1.0/5603400dbbf4?limit=1')
#print(sundance.get_24_hr_total(sundance.area_url, 0, '24_hour'))

#solitude = AreasCrawler('solitude', 'https://solitudemountain.com/')
#print(solitude.get_24_hr_total(solitude.area_url, 'type', 0))







