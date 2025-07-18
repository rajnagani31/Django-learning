from django.contrib import admin
from .models import OneTOMany,test,Teacher,student,techerstudent
# Register your models here.
@admin.register(OneTOMany)
class AdminMany(admin.ModelAdmin):
    list_display=['id','student_name','age']

@admin.register(test)
class admincheak(admin.ModelAdmin):
    list_display=[]   

@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display=['name','course']

@admin.register(student)
class AdminStudent(admin.ModelAdmin):
    list_display=['name','course_choice']  

@admin.register(techerstudent)
class AdminStudent(admin.ModelAdmin):
    list_display=['teacher','student']  