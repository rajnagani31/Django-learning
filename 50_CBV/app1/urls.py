from django.urls import path
from .views import *
from django.views.generic.base import TemplateView,RedirectView
urlpatterns= [
    path('class/',Myclass.as_view()),
    path('ac/',AsyncView.as_view()),

    # template view
    path('',TemplateView.as_view(template_name='home.html'),name='home'),

    # RediractView
    path("home/",RedirectView.as_view(url='/'),name='home1'), # rediract in template view
    path("index/",RedirectView.as_view(pattern_name='home'),name='index'), # REDIRACT ON home using pattern_name
    path("index2/",RediractviewMethod.as_view(),name='redirect in view'), # rediract using view class

    path("logging/",RediractviewLogging.as_view(),name='loggin')
]