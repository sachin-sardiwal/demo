# tjournal/models.py

from django.db import models
# Create your models here.

# add this
class Tjournal(models.Model):
    stock = models.CharField(max_length=120)
    entryprice = models.CharField(max_length=120)
    exitprice = models.CharField(max_length=120)

    def _str_(self):
        return self.stock