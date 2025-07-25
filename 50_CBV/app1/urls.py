from django.urls import path
from .views import *

urlpatterns= [
    path('class/',Myclass.as_view()),
    path('ac/',AsyncView.as_view()),
]