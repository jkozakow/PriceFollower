from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    current_lowest_price = models.FloatField()

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
