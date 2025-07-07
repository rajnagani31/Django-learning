from django.urls import path,include
from .views import set_session,get_session,delete_session
urlpatterns = [
    path('set/',set_session),
    path('get/',get_session),
    path('del/',delete_session),

]
