from django.db import models

# Create your models here.


class Course(models.Model):
    name= models.CharField(max_length=255)
    def __str__(self):
        return self.name
class student(models.Model):
    student_name=models.CharField(max_length=100)
    Course= models.ForeignKey(Course,on_delete=models.CASCADE) 

    # def __str__(self):
    #     return self.Course  
# multi choices

class course_multi(models.Model):
    choices=[
        ("AI","AI"),
        ("ML","ML"),
        ("GENAI","GenAI"),
    ]
    student_name=models.CharField(max_length=200)
    course_choice=models.CharField(choices=choices)

