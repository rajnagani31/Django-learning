from django.urls import path, include
from .views import home

urlpatterns = [path("aggr/", home, name="a")]
