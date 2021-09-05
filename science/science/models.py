from django.db import models

# Create your models here.

class user_list(models.Model):
    user = models.CharField(max_length=10)

class result(models.Model):
    user = models.CharField(max_length=10)
    question = models.CharField(max_length=10)
    answer = models.CharField(max_length=10)
    date = models.DateTimeField()
