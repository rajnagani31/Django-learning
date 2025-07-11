from django.contrib import admin
from .models import Poll,Choice
# Register your models here.
@admin.register(Poll)
class adminpoll(admin.ModelAdmin):
    list_display=('question' , 'pub_date')


@admin.register(Choice)
class adminchoices(admin.ModelAdmin):
    list_display=('poll','choice_text','votes')    