from django.urls import path
from .views import home_table

urlpatterns = [path("table/", home_table, name="table")]
