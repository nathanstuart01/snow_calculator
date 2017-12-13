# class that can be used to crawl the different ski areas for their base totals
# create a ski area class that inherits the crawl method from the base crawler class

import scrapy 
from scrapy.crawler import CrawlerProcess

class BaseSnowCrawler(scrapy.Spider):

	name = 'BaseAreaSnowCrawler'
	allowed_domains = ['alta.com']
	start_urls = 	['https://www.alta.com/']


	# design this method so the different areas can be crawled successfully, cannot be specific for only one area		
	def parse(self, response):
		ski_area_1 = 'Alta'
		#ski_area_2 = 'Grand Targhee'
		area_names_bases = [response.xpath('//span[@class="value"]/text()')[3].extract()]
		#'grandtarghee.com'
		#ski_area_2, response.xpath('//p[@class="snow-level"]/text()')[1].extract() 

		self.log('I just scraped ' + response.url)

		yield {
			'Ski Area Name': ski_area_1,
			'base_total': area_names_bases[0]
		}