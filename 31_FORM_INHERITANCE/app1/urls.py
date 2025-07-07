from django.urls import path
from .views import student, teacher

urlpatterns = [path("student/", student), path("teacher/", teacher)]
