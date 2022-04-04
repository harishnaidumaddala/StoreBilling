from django.db import models

# Create your models here.

class CartItem(models.Model):
    item = models.CharField(max_length=200)
    itemCategory = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()


