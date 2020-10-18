from django.db import models

# Create your models here.
QUESTION_TYPES = [("THEORY", "THEORY"), ("MCQ", "MCQ"),
                  ("ODD,", "OUT one out")]


class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    types = models.CharField(
        choices=QUESTION_TYPES, default="MCQ", max_length=200)
    options = models.JSONField(default=dict)
    correct_ans = models.CharField(max_length=500)


class Module(models.Model):
    moduleId = models.IntegerField()
    questions = models.ManyToManyField(Question)
