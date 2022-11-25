from django.db import models
from app.models import Category

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=45)
    unit_price = models.FloatField()