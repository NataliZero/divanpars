import scrapy


class LightingSpider(scrapy.Spider):
    name = "lighting"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru"]

    def parse(self, response):
        pass
