from django.db import models
from django.utils import timezone


class Word(models.Model):
    keyword = models.CharField(max_length=255)
    meaning = models.TextField()
    synonym = models.TextField(null=True, blank=True)
    antonym = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Word({self.keyword}, {self.meaning}, {self.synonym}, {self.antonym}, {self.date_created}'
