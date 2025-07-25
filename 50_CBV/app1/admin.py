from django.contrib import admin
from .models import NeroTech
# Register your models here.

@admin.register(NeroTech)
class AdminTech(admin.ModelAdmin):
    list_display= ['id','name','age','is_active']
    ordering=['id']