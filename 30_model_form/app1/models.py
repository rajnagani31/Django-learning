from django.db import models

# Create your models here.

class profile(models.Model):
    name=models.CharField(max_length=100,blank=True)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)