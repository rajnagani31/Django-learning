from django.contrib import admin
from nero.models import Profile,Result
# Register your models here.



class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','roll','name','email')
admin.site.register(Profile,ProfileAdmin)    


@admin.register(Result)
class resulAdmin(admin.ModelAdmin):
    list_display=('id','roll','name','CGPA')
