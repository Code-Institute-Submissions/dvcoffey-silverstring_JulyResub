from django.db import models

# Create your models here.


class Showcase(models.Model):
    name = models.CharField(max_length=254, default='', blank=True)
    start_date = models.CharField(max_length=254, default='', blank=True)
    start_time = models.CharField(max_length=254, default='', blank=True)
    location = models.CharField(max_length=254, default='', blank=True)
    entry_fee = models.CharField(max_length=254, default='', blank=True)

    def __str__(self):
        return self.name
