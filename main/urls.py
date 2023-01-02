"""Markers urls."""

from django.urls import path

from .views import MarkersMapView
from .views import search_view

app_name = "main"

urlpatterns = [
    path("map/", MarkersMapView.as_view()),
    path("search/", search_view),
]