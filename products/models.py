from __future__ import unicode_literals

from django.db import models
from clients.models import Client

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)

class Favorite(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
    
    def __srt__(self):
        return '%s %s' % (self.user.name, self.product.name)

    