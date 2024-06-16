import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-corrida-masculino#D[A:tenis%20corrida%20masculino]"]

    def parse(self, response):
        products = response.css('div.ui-search-result__content')

        for product in products:

            yield {
                'brand': product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element').get()
            }