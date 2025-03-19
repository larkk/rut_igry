from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("lab2/", include("lab2.urls")),
    path("lab3/", include("lab3.urls")),
    path("admin/", admin.site.urls),
]