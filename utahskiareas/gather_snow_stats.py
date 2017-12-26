from areas_crawler import AreasCrawler 

#alta_crawl = AreasCrawler('Alta', '', '' )
#alta_base = alta_crawl.get_base_total('https://www.alta.com/')
#snowbird_crawl = AreasCrawler('Snowbird', '', '')
#snowbird_base = snowbird_crawl.get_base_total('https://www.snowbird.com/')
brighton_crawl = AreasCrawler('Solitude', '', '')
brighton_24hr = brighton_crawl.get_base_total('https://solitudemountain.com/') 

print(brighton_24hr)