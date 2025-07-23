from django.urls import path
from .views import sync_function,async_function_view,sync_func,async_func

urlpatterns = [
    path("sync/",sync_function),
    path("async/",async_function_view),
    path("sync2/",sync_func),
    path("async2/",async_func)

]
