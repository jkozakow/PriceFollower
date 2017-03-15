from __future__ import absolute_import
from scrapy import Spider, Request
from .items import ProductItem


class ProductSpider(Spider):
    name = 'product_spider'
    base_url = 'http://www.ceneo.pl'
    start_urls = ['http://www.ceneo.pl/Komputery']
    PROD_SELECTOR = '.cat-prod-row'
    NAME_SELECTOR = '.cat-prod-row-name a ::text'
    PRICE_SELECTOR = '.price span ::text'
    URL_SELECTOR = '.cat-prod-row-name a ::attr(href)'

    def parse(self, response):
        for product in response.css(self.PROD_SELECTOR):
            product_object = ProductItem()
            product_url = self.base_url + product.css(self.URL_SELECTOR).extract_first()

            request = Request(product_url, callback=self.parse_price)
            product_object['name'] = product.css(self.NAME_SELECTOR).extract_first(),
            request.meta['product'] = product_object
            yield request

    def parse_price(self, response):
        product = response.meta['product']
        product['current_lowest_price'] = response.css(self.PRICE_SELECTOR).extract_first()
        yield product
