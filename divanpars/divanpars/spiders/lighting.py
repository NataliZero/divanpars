import scrapy

class LightingSpider(scrapy.Spider):
    name = "lighting"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/category/istochniki-osvescheniya"]  # URL страницы с источниками освещения

    def parse(self, response):
        # Находим все элементы, представляющие источники освещения
        lightings = response.css('div._Ud0k')  # Замените селектором нужного элемента
        for lighting in lightings:
            yield {
                'name': lighting.css('div.lsooF span::text').get(),  # Замените на правильный селектор для названия
                'price': lighting.css('div.pY3d2 span::text').get(),  # Замените на правильный селектор для цены
                'url': response.urljoin(lighting.css('a').attrib['href']),  # Полная ссылка на страницу товара
            }
