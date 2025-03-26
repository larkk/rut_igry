from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lab2/", include("lab2.urls")),
    path("lab3/", include("lab3.urls")),
]