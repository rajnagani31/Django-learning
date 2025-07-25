
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("app1.urls")),
    path("data/",include("sync_to_async.urls")),
    path("thread/",include("threading1.urls")),
    path("orm/",include('async_ORM.urls')),
    path("middl/",include('async_middleware.urls'))
]
