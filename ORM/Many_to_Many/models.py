from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)


class Student_course(models.Model):
    name = models.CharField(max_length=100)
    Course_select = models.ManyToManyField(Course)
