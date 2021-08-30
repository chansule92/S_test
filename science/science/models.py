from django.db import models

# Create your models here.

class result(models.Model):
    survey_idx = models.AutoField(primary_key=True)
    user = models.CharField(max_length=10)
    question_1 = models.IntegerField(1)

    def __str__(self):
        return self.text
