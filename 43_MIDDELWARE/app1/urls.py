from django.urls import path, include
from .views import home, math, user, name

urlpatterns = [
    path("home/", home),
    path("math/", math),
    path("user/", user),
    path("name/", name, name="name"),
]
