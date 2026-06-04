"""Defines URL patterns for users"""

from django.urls import path, include

from . import views

app_name = "accounts"
urlpatterns = [
    # Add the default authentication URLs
    path("", include("django.contrib.auth.urls")),
    # Registration page
    path("register/", views.register, name="register"),
]