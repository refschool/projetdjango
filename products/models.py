from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.FileField()


class Promotion(models.Model):
    code = models.CharField(max_length=5)
    description = models.CharField(max_length=100)
    reduction = models.IntegerField()