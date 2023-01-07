"""Markers urls."""

from django.urls import path

from .views import MarkersMapView

app_name = "main"

urlpatterns = [
    path("map/", MarkersMapView.as_view(),name="search"),
]