from django.contrib import admin
from .models import courses,students

@admin.register(courses)
class coursesadmin(admin.ModelAdmin):
    list_display=['course']
    
@admin.register(students)
class coursesadmin(admin.ModelAdmin):
    list_display=['name','write']