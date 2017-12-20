# class that can be used to crawl the different ski areas for their base totals
# create a ski area class that inherits the crawl method from the base crawler class

import scrapy 
from scrapy.crawler import CrawlerProcess

class TargheeSpider(scrapy.Spider):

	name = 'BaseAreaSnowCrawler'
	allowed_domains = ['grandtarghee.com']
	start_urls = 	['https://www.grandtarghee.com/']

	def parse(self, response):
		ski_area = 'Grand Targhee'
		area_name_base = response.xpath('//p[@class="snow-level"]/text()')[1].extract() 

		self.log('I just scraped ' + response.url)

		yield {
			'Ski Area Name': ski_area,
			'base_total': area_name_base
		}


# too redundant

# make a base scraper using beautiful soup

# it will pass in the name of the area I want to crawl

# the areas I want to crawl will have their selelctors saved in a  scraper lib

# i will import the scraper lib with this class as well

# the base crawler will have methods avaiable to it to get the data, parse the data, and save it to a db that corresponds to each areas primary key, their id