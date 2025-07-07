from django.urls import path
from app1.views import account_login,success
urlpatterns = [
    path('login/',account_login),
    path('success/',success),

]