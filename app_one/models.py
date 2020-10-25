from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, blank=True)
    songs = models.ManyToManyField(Song, blank=True)
    release_date = models.DateField(blank=True, null=True)

    def save(self,**kwargs):
        for song in self.songs.all():
            self.genres.add(song.genre.id)
        super(Album, self).save(**kwargs)

    def __str__(self):
        return str(self.name) + ' by ' + str(self.author)



class PlayList(models.Model):
    name = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
