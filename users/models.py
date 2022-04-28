from django.db import models

class Artist(models.Model):
    name = models.CharField()

class Album(models.Model):
    name = models.CharField()
    release_date = models.DateTimeField()
    # artist = models.ForeignKey("Artist", related_name="albums")

class Song(models.Model):
    name = models.CharField()
    duration = models.DecimalField()
    # album = models.ForeignKey("Album", related_name="songs")