from django.urls import path
from nero.views import all,single_data
urlpatterns = [
    path("all/",all),
    path("single/",single_data),


]
