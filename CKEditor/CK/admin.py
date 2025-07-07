from django.contrib import admin
from CK.models import CK

# Register your models here.
@admin.register(CK)
class CKadmin(admin.ModelAdmin):
    list_display=('title','content')