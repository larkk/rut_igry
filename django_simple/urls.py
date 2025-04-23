from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lab2/", include("lab2.urls")),
    path("lab3/", include("lab3.urls")),
    path("lab4/", include("lab4.urls")),
    path("lab5/", include("lab5.urls")),
    path("lab6/", include("lab6.urls")),
]