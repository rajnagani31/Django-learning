from django.urls import path
from .views import call_get_data

urlpatterns = [
    path("",call_get_data,name='get_data')
]
