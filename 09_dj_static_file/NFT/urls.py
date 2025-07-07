from django.urls import path
from NFT.views import NFT_django
urlpatterns = [
    path("static/",NFT_django),
]