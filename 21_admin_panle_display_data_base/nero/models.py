from django.db import models

class Profile(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255)

    # def __str__(self):
    #     return str(self.roll)

class Result(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=100)

    CGPA=models.FloatField()

    # def __str__(self):
    #     return str(self.roll)
    