# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess

# make a base module crawler that has basic crawl functionality
# make other classes/modules of crawlers that are specific to the 6 areas I want to analyze
# I want to analyze 3 different areas within rockies
# I want to analyze 3 different areas within cascadaes
# find the normal distribution/bell curve of their snow totals
# look for averages, patterns in std, mean, other data inisghts
# rockies vs cascades
# snow total too, average snow fall
# snowfall vs quanitty ?? 

# crawl snotel sites for 3 cascades sites, 3 rocky mountain sites, 3 sierra sites
# crawl historical snowfall for those three sites from areas/other sources of data
# compare totals, water densities, std in yearly snowfall
# display data on a clickable map image
# display data on a chart
# make another page for current data for six areas, showing base total, increases, yearly totals
# make base crawlers for yearly/base totals
# update these totals regularly
# six areas baker, mt hood, whistler
# alta, jackson, steamboat
# squaw, 2 other prominent, most snowfall tahoe areas


class AltaSnowTotalsSpider(scrapy.Spider):

    name = 'alta_snow_totals'
    allowed_domains = ['https://utahavalanchecenter.org/alta-monthly-snowfall']
    start_urls = ['https://docs.google.com/spreadsheet/pub?key=0AqTsmeXPVW0zdEhVZmJSa0ZqcVdRcmRGZ3FZdlNIOHc&output=html']

    def raw_snow_totals_sorter(self, snow_list):
        years = []
        totals = []
        print(years)
        print(totals) 


    def parse(self, response):
        raw_data = response
        # Set your xpath to the css element that contains the data you want to select
        snow_totals_xpath = raw_data.xpath('//td[@class="s3"]/text()').extract()
        snow_totals_list = snow_totals_xpath[5:]
        self.raw_snow_totals_sorter(snow_totals_list)




            # goal is to make this a csv that i can send to the other module to calculcate the mean/std on 
            # goal is to make a different function for each ski area, depending on name, that area goes to its specific function

            # for now all of this will be run command line, based on user input to run

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

        # make a class that imports the spider class
        # use the following=




