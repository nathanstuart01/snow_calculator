from areas_crawler import AreasCrawler 

alta_crawl = AreasCrawler('Alta', '', '' )
alta_base = alta_crawl.get_base_total('https://www.alta.com/')

print(alta_base)
print(alta_crawl.base_total)