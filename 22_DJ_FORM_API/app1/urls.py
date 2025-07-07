from django.urls import path
from app1.views import Registrations,Login
urlpatterns = [
    path("register/",Registrations),
    path("login/",Login),

]