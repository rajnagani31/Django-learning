from django.db import models

# Create your models here.

class profile(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=100)