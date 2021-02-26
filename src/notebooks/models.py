from django.db import models
from django.utils import timezone


class Note(models.Model):
    content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Note({self.content}, {self.date_created}, {self.date_updated})'
