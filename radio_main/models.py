from django.db import models
from datetime import datetime

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    date = models.IntegerField()
    artist = models.CharField(max_length=100)
    duration = models.IntegerField()

    @staticmethod
    def str_duration(dur):
        # arg : int - seconds
        # out : str - duration in hh:mm:ss
        return datetime.fromtimestamp(dur).strftime('%I:%M:%S')

    def __str__(self):
        # out =>
            # name :: album :: artiost :: date :: duration
            # Kiss it off me :: Cry :: Cigarettes after sex :: 2019 :: 4:29
        return self.name + ' :: ' + self.album + ' :: ' + self.artist + ' :: ' + self.date.__str__() + ' :: ' + Song.str_duration(self.duration)
