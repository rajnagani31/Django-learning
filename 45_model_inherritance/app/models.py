from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

# basick cheaking for Dbever postgres
class cheaking(models.Model):
    name=models.CharField(max_length=100)
    
# Model Abstract 

class Companydata(models.Model):
    name=models.CharField(max_length=100)
    join_time=models.DateField()

    class Meta:
        abstract=True

class departmendata(Companydata):
    main_manager=models.CharField(max_length=100)
    Team_member=models.IntegerField()

class employdata(Companydata):
    manger_name=models.CharField(max_length=100)
    salary=models.IntegerField()

class Stafedata(Companydata):
    name= None
    totel_department_staf=models.IntegerField()
    totel_employ=models.IntegerField()
    join_time= None

#  multi table inheritance

class Examcenter(models.Model):
    center_name=models.CharField(max_length=500)
    center_city=models.CharField(max_length=100)

class Student(Examcenter):
    student_name=models.CharField(max_length=100) 
    roll=models.IntegerField() 

class data_Student(Examcenter):
    student_name=models.CharField(max_length=100) 
    roll=models.IntegerField() 


