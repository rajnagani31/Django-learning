from django.db import models

# Create your models here.
class courses(models.Model):
    course=models.CharField(max_length=100)
    def __str__(self):
        return self.course
    


class students(models.Model):
    name=models.CharField(max_length=100)
    choices=models.ManyToManyField(courses)    

    def write(self):
        return ",".join([str(p) for p in self.choices.all()]) # convert list to string
