from django.db import models

class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    city=models.CharField(max_length=50)
    roll=models.IntegerField()
    stat=models.CharField(max_length=50)
    
    
