from django.db import models


'''
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    release_date = models.DateField()
'''


class Product(models.Model):
    title = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    description = models.TextField()
    height = models.IntegerField()
    width = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


