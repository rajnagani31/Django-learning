from django.urls import path
from stock.views import learn_django_in_stock,invest
urlpatterns = [
    path("stock/",learn_django_in_stock),
    path("invest/",invest),

]