from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
