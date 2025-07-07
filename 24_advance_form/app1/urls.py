from django.urls import path
from .views import demo_,demo_up,demo_more_up
urlpatterns = [
    path('demo/',demo_),
    path('demo_up/',demo_up),
    path('demo_more_up/',demo_more_up),


]