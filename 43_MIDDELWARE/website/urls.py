from django.urls import path
from .views import home, about, object

urlpatterns = [
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("object/", object, name="object"),
]
