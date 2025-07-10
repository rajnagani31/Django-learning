from django.contrib import admin
from .models import Teacher, Student


# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "subject")


@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "teacher")
