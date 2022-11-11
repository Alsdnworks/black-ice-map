"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters
from .models import JoinedLink
from .serializers import MarkerSerializer

class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""
    queryset=JoinedLink.objects.all()
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    serializer_class = MarkerSerializer
