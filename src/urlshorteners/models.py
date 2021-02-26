from django.db import models
from django.utils import timezone


class ShortenedUrl(models.Model):
    uuid = models.CharField(max_length=10)
    link = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'ShortenedUrl({self.uuid}, {self.link}, {self.date_created})'
