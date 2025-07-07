
from django.urls import path
from .views import login,success
urlpatterns = [
    path('login/',login),
    path('success/',success),

]