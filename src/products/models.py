from django.conf import settings
from django.db import models

# Create your models here.
class Product(models.Model):
    #user = models.ForeignKey('User', on_delete=models.PROTECT)
    title = models.CharField(max_length=30) # holds characters
    description = models.TextField(default=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return self.title

class User(models.Model):
    pass
