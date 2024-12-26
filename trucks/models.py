from django.db import models

class Truck(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre= models.CharField(max_length=100)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio_files/')
