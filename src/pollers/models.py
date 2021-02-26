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

# >>>  from polls.models import Question, Choice
# >>>  from django.utils import timezone

# >>>  Question.objects.all()
# >>>  q = Question(question_text="What is your favorite Python Framework?", pub_date=timezone.now())
# >>>  q.save()
# >>>  q.id
# >>>  q.question_text

# >>>  Question.objects.all()
# >>>  Question.objects.filter(id=1)
# >>>  Question.objects.get(pk=1)
# >>>  q = Question.objects.get(pk=1)

# >>>  q.choice_set.all()
# >>>  q.choice_set.create(choice_text='Django', votes=0)
# >>>  q.choice_set.create(choice_text='Flask', votes=0)
# >>>  q.choice_set.create(choice_text='Flask', votes=0)
# >>>  q.choice_set.all()
# >>>  quit()
