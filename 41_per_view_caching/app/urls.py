from django.urls import path 
from .views import app1,app2,app3
from django.views.decorators.cache import cache_page


urlpatterns = [
    path("app1/",app1),

    path("app2/",app2),
    path("app3/",cache_page(30)(app3)),# url base caching
    
]
