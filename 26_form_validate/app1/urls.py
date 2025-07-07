from django.urls import path
from .views import user_login,success_submit

urlpatterns = [
    path("login/",user_login),
    path("success/",success_submit)
]
