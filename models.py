from django.db import models

# Create your models here.
class AppUsers(models.Model):
    Username = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    password = models.CharField(max_length=32)
class Questions(models.Model):
    question_text = models.CharField(max_length=32)

class Answers(models.Model):
    question_text = models.CharField(max_length=32)
    Username = models.CharField(max_length=32)
    answer_text = models.TextField()
    score = models.FloatField()
