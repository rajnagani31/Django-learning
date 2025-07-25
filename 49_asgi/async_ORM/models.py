from django.db import models

# Create your models here.
class manger(models.Model):
    name=models.CharField('Student Name',max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=100)

