from django.urls import path,include
from .views import set_cooki,get_cooki,delete_cooki,set_signed,get_signed
urlpatterns = [
    path("set/",set_cooki,name="set"),
    path("get/",get_cooki,name="get"),
    path("delete/",delete_cooki,name="delete"),
    path("set_sig/",set_signed,name="delete"),
    path("get_sig/",get_signed,name="delete"),




]