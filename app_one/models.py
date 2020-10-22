from django.db import models
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' by ' + str(self.author)


class Song(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PlayList(models.Model):
    name = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
