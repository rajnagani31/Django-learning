from django.db import models

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    city=models.CharField(max_length=50)
    roll=models.IntegerField()
    stat=models.CharField(max_length=50)

    def __str__(self):
        return str(self.roll)
    
class Result(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=50)
    CGPA=models.FloatField()
    def __str__(self):
        return str(self.roll)    
    


 
