from django.contrib import admin
from .models import manger
# Register your models here.
@admin.register(manger)
class adminManager(admin.ModelAdmin):
    list_display=['id','name','age','city']
    ordering=['id']