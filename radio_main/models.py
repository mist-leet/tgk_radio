from django.db import models
from django.db.models import Model


class Song(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=300)
    # img = models.ImageField(upload_to='img', default='def.jpg')


class Cover(models.Model):
    url = models.CharField(max_length=300)
    img = models.ImageField()
