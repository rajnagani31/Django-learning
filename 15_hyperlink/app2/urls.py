from django.urls import path,include
from app2.views import django,python

urlpatterns = [
    path('dj/',django,name='dj'),
    path('py/',python,name='py'),

]