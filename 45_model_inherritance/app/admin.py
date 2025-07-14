from django.contrib import admin
from app.models import Stafedata,employdata,departmendata,Examcenter,data_Student
# Register your models here.

@admin.register(departmendata)
class departmentAdmin(admin.ModelAdmin):
    list_display=['id','name','join_time','main_manager','Team_member']


@admin.register(employdata)
class employAdmin(admin.ModelAdmin):
    list_display=['id','name','join_time','manger_name','salary']

@admin.register(Stafedata)
class employAdmin(admin.ModelAdmin):
    list_display=['id','totel_department_staf','totel_employ']


@admin.register(Examcenter)
class Examecenter(admin.ModelAdmin):
    list_display=['id','center_name','center_city']



@admin.register(data_Student)
class StudentExamecenter(admin.ModelAdmin):
    list_display=['id','student_name','roll','center_name','center_city']
