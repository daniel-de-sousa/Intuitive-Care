import scrapy


class IntuitiveSpider(scrapy.Spider):
    name = 'intuitive'
    allowed_domains = ['gov.com']
    start_urls = ['http://gov.com/']

    def parse(self, response):
        pass
