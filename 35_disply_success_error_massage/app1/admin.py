from django.contrib import admin
from .models import user
# Register your models here.
@admin.register(user)
class AdminUser(admin.ModelAdmin):
    list_display=('id','name','email','password')