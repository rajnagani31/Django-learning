from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class OneTOMany(models.Model):
    # user=models.ForeignKey(User,on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    student_name=models.CharField(max_length=100)
    age=models.IntegerField()

class test(models.Model):
    name=models.CharField(max_length=100)
    # name=models.ForeignKey(OneTOMany,max_length=100,on_delete=models.SET_NULL,null=True)
    pass

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.course}"
    
class student(models.Model):
    name=models.CharField(max_length=100)
    course_choice=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['name']   

class techerstudent(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True)
    student=models.ForeignKey(student,on_delete=models.SET_NULL,null=True)