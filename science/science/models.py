from django.db import models

# Create your models here.

class user_list(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=10)

class result(models.Model):
    user_id = models.IntegerField(max_length=10)
    user = models.CharField(max_length=10)
    question = models.CharField(max_length=10)
    answer = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True, blank=True)
