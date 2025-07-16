from django.contrib import admin
from .models import modelmanager

@admin.register(modelmanager)
class adminmanager(admin.ModelAdmin):
    list_display=['id','name','age','passing_year']