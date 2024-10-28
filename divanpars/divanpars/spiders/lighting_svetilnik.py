import scrapy

class LightingSvetilnikSpider(scrapy.Spider):
    name = "lighting_svetilnik"
    allowed_domains = ["svetilnik-online.ru"]
    start_urls = ["https://svetilnik-online.ru/catalog/svetilniki/"]

    def parse(self, response):
        items = response.css('div.catalog-item')  # Обновите селектор в соответствии с сайтом
        for item in items:
            yield {
                'name': item.css('div.catalog-item__title a::text').get(),
                'price': item.css('div.catalog-item__price span::text').get(),
                'url': response.urljoin(item.css('div.catalog-item__title a').attrib['href']),
            }

        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
