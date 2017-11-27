# crawl the current base of stevens, baker, crystal, alta, snowbird, jackson, grand targhee, mt hood meadows, squaw

# get those different base numbers

# crawl the base numbers each day

# save the base numbers to a csv or db

# display the base numbers daily

# create a function that displays the difference between yesterday and today, displays that as 24 hr snowfall

# display the base numbers as a graph

# use the base numbers from an api? Try to display the data without making an entire web application or display the data 
# using an api, rather than one single web application
# provide a link to source data, describing what elevation and aspect the bases are reported from

# 

import scrapy

class MySpider(scrapy.Spider):
	name = 'www.alta.com'
	allowed_domains = ['alta.com']
	start_urls = ['https://www.alta.com']

	def parse_item(self, response):
		alta_base_total = response.xpath('//span[@class="value]/text()').extract()
		print(alta_base_total)

alta_base = MySpider()
alta_base.parse_item()
			