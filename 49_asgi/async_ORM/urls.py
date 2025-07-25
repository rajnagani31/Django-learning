from .views import query_set

from django.urls import path

urlpatterns = [
    path('',query_set)
]
