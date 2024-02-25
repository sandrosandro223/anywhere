from django.db import models

PRIORITY =[("H","high"),("M","medium"),("L","low")]
# Create your models here.
class Question(models.Model):
    title   = models.CharField(max_length=60)
    question  = models.TextField(max_length=499)
    priority = models.CharField(max_length=1, choices=PRIORITY)


def __str__(self):
    return self.title