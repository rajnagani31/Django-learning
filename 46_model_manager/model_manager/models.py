from django.db import models
from datetime import date
from .manager import customModel,custommethod
# Create your models here.
class modelmanager(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    passing_year=models.DateField(default=date.today())

    objects=models.Manager()
    custom_manager=customModel()
    custom_method=custommethod()    
