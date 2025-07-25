from django.urls import path
from .views import start_thread
urlpatterns = [
    path("",start_thread)
]
