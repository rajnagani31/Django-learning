from django.contrib import admin
from .models import Userprofile,Profile,city
# Register your models here.


@admin.register(Userprofile)
class profileAdmin(admin.ModelAdmin):
    list_display=['id','name','roll']


@admin.register(Profile)
class profilemodel(admin.ModelAdmin):
    list_display=['name','age']    


@admin.register(city)
class citeditails(admin.ModelAdmin):
    list_display=('id','state')    