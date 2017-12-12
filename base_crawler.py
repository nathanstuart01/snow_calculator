# class that can be used to crawl the different ski areas for their base totals
# create a ski area class that inherits the crawl method from the base crawler class

import scrapy 

class BaseSnowCrawler(scrapy.Spider):

name = 'BaseAreaSnowCrawler'

# areas I would like to ski in someday, can add more later, as interests change
# Eventually add these to crawl
"""'www.jacksonhole.com', 'www.whistlerblackcomb.com', 
					'www.snowbird.com', 'www.grandtarghee.com',
					'www.wolfcreekski.com', 'www.brightonresort.com', 'www.solitudemountain.com',
					'www.squawalpine.com', 'www.steamboat.com'"""
allowed_domains= [
					'www.alta.com', 
				  ]

start_urls = 	[ 'https://www.alta.com/conditions/daily-mountain-report/snow-report'  

				]