
from django.urls import path
from .views import caching

urlpatterns = [
    path("caching/",caching)
]
