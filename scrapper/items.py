from scrapy_djangoitem import DjangoItem
from products.models import Product


class ProductItem(DjangoItem):
    django_model = Product
