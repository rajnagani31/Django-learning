from django.urls import path
from .views import async_call,sync_call


urlpatterns = [
    path('sync/',sync_call),
    path('async/',async_call)
]
