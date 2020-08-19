from django.db import models

# Create your models here.

class WorkExp(models.Model):
    startTime = models.DateField()
    endTime = models.DateField(null=True,blank=True)
    company = models.CharField(max_length=50)
    desc = models.TextField(default='')