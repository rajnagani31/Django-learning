
from django.contrib import admin
from django.urls import path,register_converter
from .views import home ,profile
from .converter import FourDigitYearConverter
register_converter (FourDigitYearConverter,'yyyy')
urlpatterns = [
    path('',home,name='home'),
    # path('profile/<my_id>',profile,name='profile'),
    # path('profile/<int:my_id>',profile,name='profile'),
    # path('profile/<int:my_class>/<int:my_id>',profile,name='profile')
    path('profile/<yyyy:year>',profile,name='profile'),



]