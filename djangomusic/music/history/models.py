from django.db import models

# Create your models here.

class Artist(models.Model):
	artist = models.CharField(max_length=100)

	def __str__(self):
		return self.artist

class Song(models.Model):
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	song = models.CharField(max_length=100)
	album = models.CharField(max_length=100)

	def __str__(self):
		return self.song
