# -*- coding: utf-8 -*-
import scrapy


class AltaSnowTotalsSpider(scrapy.Spider):
    snow_area_totals_allowed = 'https://utahavalanchecenter.org/alta-monthly-snowfall'
    snow_area_totals_to_start = 'https://docs.google.com/spreadsheet/pub?key=0AqTsmeXPVW0zdEhVZmJSa0ZqcVdRcmRGZ3FZdlNIOHc&output=html'
    snow_area_crawling = 'alta_snow_totals'
    name = snow_area_crawling
    allowed_domains = [snow_area_totals_allowed]
    start_urls = [snow_area_totals_to_start]

    def parse(self, response):
        raw_data = response
        # Set your xpath to the css element that contains the data you want to select
        snow_totals_xpath = raw_data.xpath('//td[@class="s3"]/text()').extract()

        for snow_totals in snow_totals_xpath:
            yearly_totals = []
            yearly_totals.extend(snow_totals)
            print(yearly_totals)

        # response.xpath('//td[@class="s3"]/text()').extract()
        #response.xpath('//td[@class="s1"]/text()')[8].extract()
        #fetch('https://docs.google.com/spreadsheet/pub?key=0AqTsmeXPVW0zdEhVZmJSa0ZqcVdRcmRGZ3FZdlNIOHc&output=html')
        # this gets all the data, now i need to loop through it and add the right ones to an array
        # make a spider module/scraper for all the areas i want to crawl
        # modules would have scrapers for base totals this year
        # modules would be for historical snowfall
        # try to write one spider, then turn that spider into a moduel,

        # try to make something into a class
        # what in what i am making is a class that has properties that can import modules, functions, attritrbues
        # ski area is an object
        # it has daily snowfall and historical snowfall
        # think of another class i can make to combine with this class




