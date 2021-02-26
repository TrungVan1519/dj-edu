from django.db import models
from django.utils import timezone


class Question(models.Model):
    text = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Question({self.text}, {self.date_created}, {self.date_updated})'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Choice({self.question}), {self.text}, {self.votes}, {self.date_created}, {self.date_updated})'
