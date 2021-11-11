from django.db import models


class ProductHistory(models.Model):
    price = models.IntegerField()
    check_date = models.DateTimeField()


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=120)
    actual_price = models.IntegerField()
    price_history = models.ForeignKey(ProductHistory, on_delete=models.CASCADE)


class Scrapper(models.Model):

    url = models.URLField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
