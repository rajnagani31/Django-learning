from django.urls import path
from app1.views import register,add,login
urlpatterns = [
    path("register/",register),
    path("address/",add),
    path("login",login)

]
