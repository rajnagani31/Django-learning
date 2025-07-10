from django.contrib import admin
from .models import underConstruction

# Register your models here.


@admin.register(underConstruction)
class adminUnder(admin.ModelAdmin):
    list_display = (
        "id",
        "Uc_note",
        "uc_duration",
        "is_under_construction",
    )
