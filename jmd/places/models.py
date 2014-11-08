from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120)
    uid = models.CharField(max_length=120)


class Place(models.Model):
    venue_uid = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    lat = models.FloatField()
    lng = models.FloatField()




