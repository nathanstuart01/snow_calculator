from areas_crawler import AreasCrawler 

alta_crawl = AreasCrawler('Alta', '', '' )
#alta_base = alta_crawl.get_base_total('https://www.alta.com/')
snowbird_crawl = AreasCrawler('Snowbird', '', '')
snowbird_base = snowbird_crawl.get_base_total('https://www.snowbird.com/')

print(snowbird_base)