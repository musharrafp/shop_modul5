from unicodedata import category

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=222)
    dec = models.CharField(max_length=222)
    image = models.ImageField(null=True, blank=True, upload_to='img')
    category = models.CharField(max_length=222)

class Product(models.Model):
    title = models.CharField(max_length=222)
    price = models.CharField(max_length=222)
    dec = models.CharField(max_length=223)
    image = models.ImageField(null=True, blank=True, upload_to='images')

    def __str__(self):
        return self.title
