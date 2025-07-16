from django.urls import path
from .views import city_data
urlpatterns = [
    path("",city_data)
]
