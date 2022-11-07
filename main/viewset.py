"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters

from .models import JoinedLink
from .serializers import MarkerSerializer

class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""
    from django.db import connection
    cursor=connection.cursor()
    cursor.execute("DELETE from public.main_marker where (now() - date) < interval '6 hour'; TRUNCATE main_joinedlink; INSERT INTO main_joinedlink overriding system value select main_link.id+1, main_link.location, main_marker.stat from main_link,main_marker  where ST_CONTAINS(main_link.location, main_marker.location);")
    connection.close() 
    queryset=JoinedLink.objects.all()
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    serializer_class = MarkerSerializer
