from django.db import models
from django.db.models.fields import DateTimeCheckMixin, DateTimeField


class Song(models.Model):
    cover = models.ImageField(upload_to='song/cover', blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    artist = models.CharField(max_length=255, blank=False, null=False)
    feat = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Title: {self.title} by: {self.artist}"
