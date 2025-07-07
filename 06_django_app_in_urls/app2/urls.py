
from django.urls import path
from app2.views import read
urlpatterns = [
    path("about",read),
]
