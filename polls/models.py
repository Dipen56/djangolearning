from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
# A model is essentially, your database layout, with additional metadata
class Qestion(models.Model):
    #database feilds for qestion table
    qestion_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    #database feilds for choice table
    qestion = models.ForeignKey(Qestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text