from django.contrib import admin
from .models import Course, Student_course

# Register your models here.


@admin.register(Course)
class CourseDitails(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Student_course)
class CourseStudent(admin.ModelAdmin):
    list_display = ("id", "name")
