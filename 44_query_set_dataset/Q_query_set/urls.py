from django.urls import path
from .views import Q_set

urlpatterns = [path("q/", Q_set)]
