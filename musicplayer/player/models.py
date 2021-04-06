from django.db import models
from django.db.models.fields import DateTimeCheckMixin, DateTimeField


class Artist(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255, blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.artist}"


class Song(models.Model):
    cover = models.ImageField(upload_to='song/cover', blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    feat = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Title: {self.title} by: {self.artist}"
