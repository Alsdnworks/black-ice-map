"""Markers API URL Configuration."""

from rest_framework import routers

from .viewset import MarkerViewSet

router = routers.DefaultRouter()
router.register(r"markers", MarkerViewSet)

urlpatterns = router.urls
