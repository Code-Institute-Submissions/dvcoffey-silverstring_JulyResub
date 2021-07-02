from django.db import models
from products.models import Product


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews',
        null=True, on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=200)
    review = models.TextField(max_length=800)

    def __str__(self):
        return self.name
