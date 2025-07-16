from django.contrib import admin
from NF1.models import Course,student,course_multi
# Register your models here.

@admin.register(Course)
class couresmodel(admin.ModelAdmin):
    list_disply=['id','name']

@admin.register(student)
class couresStudentmodel(admin.ModelAdmin):
    list_disply=['id','student_name',"Course"]

@admin.register(course_multi)
class choicemulti(admin.ModelAdmin):
    list_display=['id','student_name','course_choice']