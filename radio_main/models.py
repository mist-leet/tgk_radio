from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cover(models.Model):
    img = models.ImageField(upload_to='static/img')
    songs = models.ManyToManyField(Song)
