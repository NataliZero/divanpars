import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        # Находим все элементы, представляющие диваны
        divans = response.css('div._Ud0k')  # Замените селектором нужного элемента
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span::text').get(),  # Замените на правильный селектор для названия
                'price': divan.css('div.pY3d2 span::text').get(),  # Замените на правильный селектор для цены
                'url': divan.css('a').attrib['href'],  # Ссылка на страницу товара
            }
