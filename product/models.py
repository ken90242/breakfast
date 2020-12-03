from django.db import models
from shop.models import Shop

# Create your models here.
class Product(models.Model):
    stock_pcs = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    vip = models.BooleanField()
