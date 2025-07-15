from django.contrib import admin
from proxy.models import Product,Product2
# Register your models here.


@admin.register(Product)
class productdata(admin.ModelAdmin):
    list_display=['id','name','price']
    
@admin.register(Product2)
class productdata2(admin.ModelAdmin):
    list_display=['id','name','price']
    list_filter=['price']    