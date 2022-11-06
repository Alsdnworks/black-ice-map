"""Markers API views."""
from rest_framework import viewsets
from rest_framework_gis import filters
from django.db import connection
from .models import JoinedLink
from .models import Marker
from .serializers import MarkerSerializer


class MarkerViewSet(viewsets.ReadOnlyModelViewSet):
    """Marker view set."""
    cursor=connection.cursor()
    cursor.execute("""
                TRUNCATE main_joinedlink;
                INSERT INTO main_joinedlink 
                select main_link.id, main_link.link_id, main_marker.name, main_link.location 
                from main_link,main_marker 
                where ST_CONTAINS(main_link.location, main_marker.location);
                   """)
    queryset=JoinedLink.objects.all()
    connection.close() 
    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = JoinedLink.objects.all()
    serializer_class = MarkerSerializer
