import scrapy

class LightingVamsvetSpider(scrapy.Spider):
    name = "lighting_vamsvet"
    allowed_domains = ["vamsvet.ru"]
    start_urls = ["https://www.vamsvet.ru/catalog/svetilniki/"]

    def parse(self, response):  # Измените сигнатуру метода
        # Находим все элементы, представляющие источники освещения
        items = response.css('div.product-card')  # Замените на селектор, соответствующий структуре сайта
        for item in items:
            yield {
                'name': item.css('h3.product-title a::text').get(),  # Замените на селектор для названия
                'price': item.css('span.price::text').get(),  # Замените на селектор для цены
                'url': response.urljoin(item.css('h3.product-title a').attrib['href']),  # Полная ссылка на товар
                'image_url': item.css('img.product-img::attr(src)').get(),  # Замените на селектор для картинки
                'description': item.css('p.product-desc::text').get(),  # Замените на селектор для описания
                # Добавьте другие необходимые поля, как описано выше
            }

        # Пагинация: находим ссылку на следующую страницу и переходим к ней
        next_page = response.css('a.next-page::attr(href)').get()  # Обновите селектор для кнопки следующей страницы
        if next_page:
            yield response.follow(next_page, callback=self.parse)

