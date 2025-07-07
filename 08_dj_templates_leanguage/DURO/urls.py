from django.urls import path
from DURO.views import django,date_time,float,if_tag,loop,complex
urlpatterns = [
    path("duro/",django),
    path("date/",date_time),
    path("float/",float),
    path("if/",if_tag),
    path("loop/",loop),
    path("com/",complex),





]