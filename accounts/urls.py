"""Defines URL patterns for users"""

from django.urls import path, include

app_name = "accounts"
urlpatterns = [
    # Add the default authentication URLs
    path("", include("django.contrib.auth.urls")),
]