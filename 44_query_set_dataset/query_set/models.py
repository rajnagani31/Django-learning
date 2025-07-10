from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_num = models.CharField(max_length=3)
    city = models.CharField(max_length=50)
    marks = models.IntegerField()
    passing_year = models.DateField()


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
