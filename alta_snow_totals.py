# -*- coding: utf-8 -*-
import scrapy


class AltaSnowTotalsSpider(scrapy.Spider):
    name = 'alta_snow_totals'
    allowed_domains = ['https://utahavalanchecenter.org/alta-monthly-snowfall']
    start_urls = ['https://utahavalanchecenter.org/alta-monthly-snowfall/']

    def parse(self, response):
        raw_data = response.body
        response.xpath('//td[@class="s3"/text()').extract()
