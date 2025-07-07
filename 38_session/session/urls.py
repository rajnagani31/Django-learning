from django.urls import path
from .views import set_session,get_session,delete_session,flush_session

urlpatterns = [
    path('set/',set_session),
    path('get/',get_session),
    path('del/',delete_session),
    path('flush/',flush_session),

]
