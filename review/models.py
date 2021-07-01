from django.db import models
from products.models import Product
from django.utils import timezone


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews',
        null=True, on_delete=models.SET_NULL)
    name = models.CharField(
        max_length=200)
    review = models.TextField(max_length=800)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
