# class that can be used to crawl the different ski areas for their base totals
# create a ski area class that inherits the crawl method from the base crawler class

import scrapy 
from scrapy.crawler import CrawlerProcess

class AltaSpider(scrapy.Spider):

	name = 'BaseAreaSnowCrawler'
	allowed_domains = ['alta.com']
	start_urls = 	['https://www.alta.com/']

	def parse(self, response):
		ski_area = 'Alta'
		area_name = response.xpath('//span[@class="value"]/text()')[3].extract()


		self.log('I just scraped ' + response.url)

		yield {
			'Ski Area Name': ski_area,
			'base_total': area_name
		}
