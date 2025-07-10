from django.contrib import admin
from .models import Teacher, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "subject", "city")


@admin.register(Student)
class student(admin.ModelAdmin):
    list_display = ("id", "name", "roll_num", "city", "marks", "passing_year")
