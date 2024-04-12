from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    
class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200, null=True)
    milliseconds = models.IntegerField(default=0)
    bytes = models.IntegerField(default=0)
    unitPrice = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)