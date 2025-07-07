from django.urls import path,include
from course.views import learun_django,learun_python

urlpatterns = [
    path('dj/',learun_django),
    path('py/',learun_python),

]