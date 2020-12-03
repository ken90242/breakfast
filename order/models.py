from django.db import models
from shop.models import Shop
from product.models import Product

# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.CharField(max_length=100, default=None)
    qty = models.PositiveIntegerField()
